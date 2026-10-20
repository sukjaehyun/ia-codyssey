# 미션 2-2 — API를 조합한 국내 여행 추천

Python CLI에서 여행 날짜를 입력하면 **OpenAI 추천 JSON → Kakao Local 맛집 검색 → OpenAI 일정 생성 → 최종 Markdown 리포트 저장** 순서로 실행합니다. Python 3.10 이상과 표준 라이브러리만 사용합니다. 추가 패키지 설치가 필요 없습니다.

## 실행 준비

이 폴더로 이동한 뒤 Python 버전을 확인하세요. macOS/Linux에서 `python` 대신 `python3`, Windows에서는 필요하면 `py -3`를 사용하세요.

```sh
python --version
```

OpenAI API 키와 Kakao Developers 앱의 **REST API 키**가 필요합니다. Kakao의 JavaScript 키나 Admin 키를 사용하지 마세요. 사용 계정의 API 권한과 쿼터를 확인하세요. OpenAI 모델은 기본 `gpt-4.1-mini`이며 `OPENAI_MODEL`로 접근 가능한 Responses/Structured Outputs 지원 모델로 바꿀 수 있습니다.

### API 키 설정

macOS/Linux의 현재 터미널에서 입력값이 화면이나 명령 이력에 남지 않도록 설정하려면 다음을 실행하세요. 실제 키는 명령 실행 후 숨겨진 입력에 붙여넣습니다.

```sh
bash
read -r -s -p "OpenAI API key: " OPENAI_API_KEY; echo
export OPENAI_API_KEY
read -r -s -p "Kakao REST API key: " KAKAO_REST_API_KEY; echo
export KAKAO_REST_API_KEY
```

또는 현재 세션에서 환경변수를 직접 설정할 수 있습니다. 아래 값은 설정 방식 설명용이며 실제 키가 아닙니다. 직접 입력하면 셸 이력에 남을 수 있습니다.

```sh
export OPENAI_API_KEY="YOUR_KEY"
export KAKAO_REST_API_KEY="YOUR_KEY"
```

Windows PowerShell에서는 다음처럼 설정합니다. 실제 키를 넣은 명령이 이력이나 스크린샷에 남지 않도록 주의하세요.

```powershell
$env:OPENAI_API_KEY="YOUR_KEY"
$env:KAKAO_REST_API_KEY="YOUR_KEY"
```

`.env.example`은 변수 목록 안내용입니다. 이 프로그램은 **환경변수만 읽으며 .env 파일을 자동으로 로드하지 않습니다.** 키는 코드, README, Git 커밋, 채팅, 결과 파일에 작성하지 마세요. 환경변수를 쓰면 협업 중 키 공개를 막고 코드 수정 없이 키를 교체할 수 있으며, 과금·쿼터 사고를 줄일 수 있습니다. `.gitignore`는 실수로 만드는 `.env`와 실행 결과를 기본 제외합니다. 이미 커밋된 키는 ignore로 제거되지 않으므로 즉시 폐기·재발급해야 합니다.

## 실제 API 실행

```sh
python travel_planner.py -date "2026-10-25"
# --date도 지원합니다.
python travel_planner.py --date "2026-10-25"
```

날짜 형식과 실제 존재 여부를 확인합니다. `2026-02-30`, `2026-1-1`, 날짜 옵션 누락은 사용법을 출력하고 종료 코드 2로 끝납니다. 키 누락은 API 호출 전에 설정할 변수명을 출력하고 종료 코드 1로 끝납니다.

정상 실행에서 LLM을 2회 호출하며, 추천 JSON 검증 실패 시에만 최대 1회 추가 호출합니다. 지도 요청은 1회입니다. 실제 호출은 API 비용·쿼터를 사용할 수 있습니다. 실시간 예보나 행사 검색 API는 쓰지 않으므로 날씨는 일반적인 계절 설명이고 행사는 확인이 필요한 후보입니다.

### 키 없이 실행 흐름 확인

```sh
python travel_planner.py -date "2026-10-25" --demo
```

데모는 고정 예시 추천과 맛집 0건을 사용합니다. 네트워크를 호출하지 않습니다. 날짜별 실제 추천이나 실제 API 성공 증빙으로 제출할 수 없습니다. `results/sample_demo_*`는 이 모드로 실제 생성한 예시 파일입니다.

## 출력 확인

기본 출력 경로는 **프로그램 파일 옆 `results/`** 입니다. `--output-dir 경로`로 변경할 수 있습니다. 파일명에는 실행 시각(로컬 시간대, 마이크로초 포함)과 여행 날짜가 모두 들어가 같은 날짜를 재실행해도 기존 파일을 덮어쓰지 않습니다.

- `실행시각_여행날짜_raw.json`: 여행 날짜, 실행 시각, 제공자, 실행 모드, 상태, 1차 추천 `recommendation`, 맛집 `restaurants`, `errors` 배열
- `실행시각_여행날짜_travel_plan.md`: 추천 지역·이유, 날씨, 행사 후보, 맛집/주소/좌표/지도 URL, 오전·오후·저녁 일정, 오류 요약
- `mode=live`는 실제 API 실행, `mode=demo`는 고정 예시 실행입니다.
- JSON은 API 응답에서 추출·파싱한 데이터입니다. 인증 헤더와 제공자 응답 전체는 저장하지 않습니다.

맛집의 `name`, `address`, `category`, `url`, `x`(경도), `y`(위도)를 저장합니다. 가능한 좌표는 숫자로 변환하며, 제공되지 않은 좌표는 `null`입니다. 추천 도시를 `도시명 맛집` 검색어와 음식점 카테고리 `FD6`로 전달하여 최대 5곳을 검색합니다. 관련도 기반 검색이므로 정확한 행정구역 포함 여부와 영업 여부는 지도에서 확인하세요.

## 오류 정책

| 상황 | 동작 |
|---|---|
| 키 미설정 | 요청 전 즉시 종료, 설정 변수 안내 |
| 추천 JSON 파싱/필수 키/타입 오류 | 필수 JSON 출력 재요청 1회, 다시 실패하면 종료·오류 JSON 보존 |
| LLM 인증/쿼터/네트워크/거절·미완료 | 종료 코드 1, 오류 JSON 보존 |
| 지도 0건 | errors에 EMPTY_RESULT, 데이터 없음으로 리포트 생성 계속 |
| 지도 인증/쿼터/네트워크/파싱 실패 | errors에 요약, 데이터 없음으로 리포트 생성 계속 |
| 마지막 LLM 실패/일정 형식 오류 | 추천·맛집 JSON 보존, 실패를 명시한 부분 리포트 저장, 종료 코드 1 |
| 파일 저장 실패 | 경로·권한·공간 확인 안내, 종료 코드 1 |

HTTP 401/403은 키 종류·헤더·권한·앱 설정, 429는 쿼터·호출 제한을 확인하세요. 각 HTTP 요청은 60초 제한이며 무한 재시도하지 않습니다. 오류 로그에는 응답 본문이나 인증 헤더를 출력하지 않고, 결과 저장 시 알려진 키 값을 가립니다. JSON의 `status=failed`나 부분 리포트는 정상 완료 결과와 구분해야 합니다.

## 테스트

```sh
python -m unittest -v
```

실제 API 대신 모의 응답으로 날짜/누락 옵션, 키 누락, JSON 1회 재시도, 잘못된 스키마, HTTP 인증·쿼터·네트워크 오류, 장소 필드 변환, 0건·지도 실패 후 계속 진행, 리포트 섹션, 최종 실패 시 데이터 보존, 데모 무호출, 키 가림을 확인합니다.

**검증 범위:** 자동 테스트와 데모 실행은 완료할 수 있지만 실제 API 키를 사용한 통합 검증은 별도입니다. 키가 없는 상태에서 실제 응답이나 실제 맛집 정보를 만들었다고 주장하지 않습니다.

## 학습 정리

REST 요청은 URL, HTTP 메서드, 인증 헤더, 필요에 따른 본문으로 구성되고 응답은 상태 코드와 JSON 등을 포함합니다. Kakao 검색은 GET으로 쿼리 문자열을 보내 데이터를 조회하며, OpenAI는 POST로 모델·입력·JSON 출력 스키마를 본문에 보내 생성을 요청합니다. 인증 키는 두 서비스 모두 헤더로 전달합니다.

추천은 JSON Schema로 형식을 요구하고, 응답에서 텍스트를 꺼내 `json.loads()` 및 필수 키/타입 검사로 검증합니다. 검증한 `recommended_city`를 장소 검색 입력에 연결하고, 그 결과와 추천 데이터를 최종 LLM 일정 입력으로 전달합니다. 리포트의 사실 섹션은 원본 데이터로 구성하고 LLM이 오전·오후·저녁 일정을 제안합니다.

## 제출 체크리스트

- [ ] 본인 환경에서 Python 3.10 이상 확인
- [ ] 환경변수 설정 후 데모 옵션 없이 실제 API 실행
- [ ] `results/`의 `mode=live`, `status=completed` JSON과 Markdown 확인
- [ ] API 키·인증 헤더가 없는 결과만 선택하여 제출
- [ ] 실행 로그 및 결과 저장 경로 화면 촬영
- [ ] 추천 지역·날씨·행사·맛집(없으면 데이터 없음)·일정·errors 확인

실행 결과는 기본 Git 추적 제외입니다. 실제 결과를 저장소에 제출할 때는 키와 민감 정보가 없는지 확인한 파일만 선택해 강제 추가하세요.

```sh
git add -f "미션 2-2/results/실제파일명_raw.json" "미션 2-2/results/실제파일명_travel_plan.md"
```

위 `git add`는 저장소 루트 기준입니다. 이 프로그램에는 선택 과제인 복수 지역 추천과 캐싱은 포함하지 않았습니다.

## 공식 참고 문서

- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses)
- [Kakao Local REST API](https://developers.kakao.com/docs/ko/local/dev-guide#search-by-keyword)
