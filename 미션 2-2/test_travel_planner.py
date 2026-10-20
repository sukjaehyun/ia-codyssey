"""실제 네트워크/비용 없이 핵심 정책을 검증하는 표준 unittest."""
import argparse
import contextlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
import travel_planner as app

REC = {"recommended_city": "강릉", "weather": "가을 날씨", "events": ["행사 후보"], "reason": "바다가 있습니다. 산책하기 좋습니다."}
SCHEDULE = "### 오전\n산책\n### 오후\n관람\n### 저녁\n식사"
KEYS = {"OPENAI_API_KEY": "test-only-openai", "KAKAO_REST_API_KEY": "test-only-kakao"}


class PlannerTests(unittest.TestCase):
    def test_date_validation(self):
        self.assertEqual(app.parse_date("2028-02-29"), "2028-02-29")
        for value in ["2026-02-29", "2026-13-01", "2026-1-01", "wrong", "2026-10-20extra"]:
            with self.subTest(value=value), self.assertRaises(argparse.ArgumentTypeError):
                app.parse_date(value)

    def test_cli_missing_or_invalid_date(self):
        for argv in ([], ["-date", "2026-02-30"]):
            with self.subTest(argv=argv), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                app.main(argv)
            self.assertEqual(caught.exception.code, 2)

    def test_missing_keys_stops_before_network(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(app, "request_json") as request, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(app.main(["-date", "2026-10-20"]), 1)
        request.assert_not_called()

    def test_json_retry_once(self):
        errors = []
        with patch.object(app, "llm_text", side_effect=["bad", json.dumps(REC)]) as llm, contextlib.redirect_stdout(io.StringIO()):
            result = app.recommend("2026-10-20", "test", "model", errors)
        self.assertEqual(result, REC)
        self.assertEqual(llm.call_count, 2)
        self.assertEqual(len(errors), 1)

    def test_wrong_schema_retries_only_once(self):
        with patch.object(app, "llm_text", return_value='{"events": []}') as llm, contextlib.redirect_stdout(io.StringIO()), self.assertRaises(app.APIError):
            app.recommend("2026-10-20", "test", "model", [])
        self.assertEqual(llm.call_count, 2)

    def test_llm_auth_no_retry(self):
        with patch.object(app, "llm_text", side_effect=app.APIError("AUTH_ERROR", "HTTP 401")) as llm, self.assertRaises(app.APIError):
            app.recommend("2026-10-20", "test", "model", [])
        self.assertEqual(llm.call_count, 1)

    def test_http_and_network_errors(self):
        for error, expected in [(HTTPError("https://example.invalid", 401, "", {}, None), "AUTH_ERROR"),
                                (HTTPError("https://example.invalid", 429, "", {}, None), "QUOTA_ERROR"),
                                (URLError("offline"), "NETWORK_ERROR")]:
            with self.subTest(expected=expected), patch.object(app, "urlopen", side_effect=error), self.assertRaises(app.APIError) as caught:
                app.request_json("https://example.invalid", {})
            self.assertEqual(caught.exception.kind, expected)

    def test_response_extraction_and_schema(self):
        response = {"status": "completed", "output": [{"type": "message", "content": [{"type": "output_text", "text": json.dumps(REC)}]}]}
        with patch.object(app, "request_json", return_value=response) as request:
            text = app.llm_text("prompt", "test", "model", True)
        self.assertEqual(json.loads(text), REC)
        self.assertEqual(request.call_args.args[2]["text"]["format"]["type"], "json_schema")
        with patch.object(app, "request_json", return_value={"status": "incomplete"}), self.assertRaises(app.APIError):
            app.llm_text("prompt", "test", "model")

    def test_place_fields_and_query(self):
        doc = {"place_name": "테스트 식당", "address_name": "강릉시 테스트 주소", "category_name": "음식점", "place_url": "https://place.map.kakao.com/123", "x": "128.9", "y": "37.7"}
        with patch.object(app, "request_json", return_value={"documents": [doc]}) as request:
            places = app.search_places("강릉", "test", [])
        self.assertIsInstance(places[0]["x"], float)
        self.assertEqual(places[0]["address"], doc["address_name"])
        self.assertIn("category_group_code=FD6", request.call_args.args[0])
        self.assertEqual(request.call_args.args[1]["Authorization"], "KakaoAK test")

    def test_zero_and_failed_places(self):
        for response in ({"documents": []}, {"documents": "bad"}, {"documents": [{"place_name": "x", "address_name": "y", "x": "nan"}]}):
            errors = []
            with patch.object(app, "request_json", return_value=response), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(app.search_places("강릉", "test", errors), [])
            self.assertTrue(errors)

    def test_pipeline_continues_on_map_failure(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ, KEYS), patch.object(app, "recommend", return_value=REC), patch.object(app, "request_json", side_effect=app.APIError("AUTH_ERROR", "HTTP 401")), patch.object(app, "itinerary", return_value=SCHEDULE) as final, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(app.main(["-date", "2026-10-20", "--output-dir", temp]), 0)
            final.assert_called_once()
            data = json.loads(next(Path(temp).glob("*.json")).read_text())
            report = next(Path(temp).glob("*.md")).read_text()
            self.assertEqual(data["status"], "completed")
            self.assertEqual(data["errors"][0]["type"], "AUTH_ERROR")
            self.assertIn("데이터 없음", report)
            for heading in ["추천 지역", "추천 이유", "날씨 요약", "행사/축제", "맛집 추천", "1일 일정", "오류 요약"]:
                self.assertIn(heading, report)

    def test_final_failure_preserves_data(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ, KEYS), patch.object(app, "recommend", return_value=REC), patch.object(app, "search_places", return_value=[]), patch.object(app, "itinerary", side_effect=app.APIError("QUOTA_ERROR", "HTTP 429")), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(app.main(["-date", "2026-10-20", "--output-dir", temp]), 1)
            data = json.loads(next(Path(temp).glob("*.json")).read_text())
            self.assertEqual(data["recommendation"], REC)
            self.assertEqual(data["status"], "failed")
            self.assertTrue(list(Path(temp).glob("*.md")))

    def test_report_format_checked(self):
        with patch.object(app, "llm_text", return_value="missing headings"), self.assertRaises(app.APIError):
            app.itinerary(REC, [], "test", "model")

    def test_demo_without_network(self):
        with tempfile.TemporaryDirectory() as temp, patch.dict(os.environ, {}, clear=True), patch.object(app, "request_json") as request, contextlib.redirect_stdout(io.StringIO()):
            for _ in range(2):
                self.assertEqual(app.main(["--date", "2026-10-20", "--demo", "--output-dir", temp]), 0)
            self.assertEqual(len(list(Path(temp).glob("*.json"))), 2)
            data = json.loads(next(Path(temp).glob("*.json")).read_text())
            self.assertEqual(data["mode"], "demo")
            self.assertEqual(data["restaurants"], [])
            request.assert_not_called()

    def test_secret_redaction(self):
        self.assertEqual(app.redact("a SECRET b", ["SECRET"]), "a [REDACTED] b")


if __name__ == "__main__":
    unittest.main()
