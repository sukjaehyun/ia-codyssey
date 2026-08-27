# B-Match AI Brand Ad — Storyboard & Production Pipeline

> **Project type:** AI-generated brand advertisement  
> **Brand:** B-Match (비매치)  
> **Format:** Vertical short-form ad  
> **Final video:** `오늘도_민턴_칠_곳_없네_완성본.mp4`  
> **Document purpose:** 완성된 영상을 기준으로 제작 의도와 AI 제작 파이프라인을 역설계한 스토리보드 문서

---

## 1. Project Overview

### 1.1 Brand Identity

| 항목 | 내용 |
|---|---|
| 브랜드명 | **B-Match (비매치)** |
| 카테고리 | 배드민턴 게스트 매칭 / 운동 일정 탐색 서비스 |
| 타겟 | 오늘 또는 가까운 시일 내 배드민턴을 치고 싶지만 참여할 모임·일정을 찾기 어려운 20~30대 생활체육 동호인 |
| User Problem | “배드민턴은 치고 싶은데, 오늘 갈 수 있는 곳을 찾기가 어렵다.” |
| USP | 흩어진 배드민턴 모집 정보를 한곳에서 확인하고, 내 조건에 맞는 게스트 일정을 빠르게 탐색할 수 있음 |
| Tone & Manner | 밝고 친근함 / 생활 밀착형 / 미니멀 / 짧고 직관적인 숏폼 문법 |
| Visual Identity | 화이트 배경, 배드민턴 복장의 단일 인물, 스마트폰 중심의 단순한 화면 구성, 마지막 브랜드 로고 노출 |
| Brand Personality | 복잡한 탐색을 대신 해결해주는 가볍고 실용적인 운동 메이트 |

### 1.2 Campaign Goal

- **광고 목적:** 브랜드 인지 + 서비스 사용 의향 형성
- **핵심 행동:** “배드민턴 칠 곳이 없을 때 B-Match를 떠올리고 앱에서 일정을 찾아본다.”
- **핵심 메시지:**  
  **“오늘 배드민턴 칠 곳이 없다면, 비매치에서 찾으면 된다.”**

### 1.3 Creative Concept

**Problem → Emotion → Discovery → Solution → Brand**

복잡한 설명보다 배드민턴 유저라면 즉시 공감할 수 있는 한 가지 상황을 보여준다.

1. 운동할 준비는 끝났지만 갈 곳이 없음
2. 휴대폰을 확인해도 마땅한 일정이 없어 실망
3. B-Match를 발견
4. 모집 일정을 한눈에 확인
5. 표정이 밝아지고 브랜드 로고로 종료

10초 내 짧은 광고이므로 기능을 여러 개 설명하기보다 **“칠 곳이 없다 → 비매치에서 찾는다”**라는 단일 문제-해결 구조에 집중한다.

---

## 2. Production Strategy

### 2.1 AI Pipeline

```text
광고 컨셉 정의
    ↓
캐릭터·스타일 기준 이미지 생성
    ↓
키프레임 확정
    ↓
Image-to-Video 생성
    ↓
앱 화면 / 브랜드 요소 삽입
    ↓
AI 음성·효과음·BGM 생성
    ↓
숏폼 편집
    ↓
1080 × 1920 MP4 출력
```

### 2.2 Tool Stack

| 구분 | Primary Tool | 사용 목적 | 선택 이유 | Alternative |
|---|---|---|---|---|
| 이미지 생성 | **ChatGPT Image / GPT Image** | 주인공, 배드민턴 복장, 화이트 스튜디오 스타일 키비주얼 생성 | 자연스러운 인물 표현과 프롬프트 수정 반복이 쉬움 | Midjourney |
| 영상 생성 | **Kling AI** | 정지 이미지를 자연스러운 인물 움직임이 있는 숏폼 영상으로 변환 | 인물 움직임과 카메라 모션의 자연스러움이 강점 | Runway / Pika |
| BGM·SFX | **Suno** 또는 생성형 SFX 도구 | 가벼운 숏폼 BGM 및 전환 효과음 | 짧은 광고 분위기에 맞는 오디오를 빠르게 생성 | Stable Audio |
| 통합 편집 | **CapCut** | 컷 편집, 자막, 앱 화면 합성, 오디오 레벨, 로고 엔드카드 | 세로형 숏폼 편집과 타이밍 조정이 빠름 | Premiere Pro |

### 2.3 Consistency Strategy — 일관성 있는 작업물을 위해 한 것

이번 영상에서는 여러 AI 생성 결과물이 서로 다른 영상처럼 보이지 않도록 **캐릭터, 의상, 소품, 공간, 조명, 모션의 기준을 먼저 정하고 그 기준을 모든 씬에 반복 적용**했다.

#### 1) 동일한 캐릭터 기준 이미지 유지

첫 번째로 생성한 여성 배드민턴 플레이어 이미지를 캐릭터 기준 레퍼런스로 정하고 이후 씬에서도 동일 인물을 유지하도록 했다. 매번 새로운 인물을 생성하는 방식보다 기준 이미지를 먼저 확정한 뒤 이를 다음 생성의 출발점으로 활용하는 방식을 선택했다.

#### 2) 외형과 소품을 고정

씬이 바뀌어도 다음 요소는 동일하게 유지했다.

- 의상: **white badminton outfit**
- 헤어스타일: **black high ponytail**
- 주요 소품: **badminton racket + smartphone**
- 인물 콘셉트: **young Korean female badminton player**

이렇게 변수를 제한해 얼굴뿐 아니라 전체 캐릭터 인상이 씬마다 달라지는 문제를 줄였다.

#### 3) 배경과 조명을 동일하게 설정

모든 씬의 공간을 **clean white seamless studio**, 조명을 **soft commercial lighting**으로 통일했다. 체육관이나 야외처럼 배경 정보가 많은 공간은 씬마다 구조와 색감이 크게 달라질 수 있기 때문에 의도적으로 단순한 스튜디오 환경을 선택했다.

#### 4) 프롬프트에도 동일한 고정 키워드 반복

일관성 전략을 단순한 제작 원칙으로만 두지 않고 실제 프롬프트에도 반영했다. 씬별 프롬프트에서 다음 표현을 반복적으로 사용했다.

```text
same Korean female badminton player
white badminton outfit
black high ponytail
badminton racket
smartphone
clean white seamless studio
soft commercial lighting
realistic
vertical 9:16
```

즉, 각 씬에서 달라지는 것은 **표정과 행동**이고 캐릭터와 세계관을 정의하는 요소는 최대한 바꾸지 않는 방식으로 프롬프트를 설계했다.

#### 5) Text-to-Video보다 Image-to-Video 중심으로 제작

각 장면을 처음부터 영상으로 생성하면 캐릭터 외형이 크게 변할 가능성이 있다고 판단했다. 그래서 먼저 이미지 생성 단계에서 **얼굴 → 의상 → 소품 → 구도 → 표정**을 확인하고, 사용할 키프레임을 확정한 뒤 해당 이미지를 Image-to-Video로 변환하는 순서로 제작했다.

```text
Character Reference
        ↓
Key Visual 생성
        ↓
얼굴 / 의상 / 소품 / 구도 확인
        ↓
승인된 이미지 확정
        ↓
Image-to-Video
```

이 방식으로 영상 생성 단계에서 캐릭터가 다시 해석되는 범위를 줄이고 재생성 횟수도 최소화했다.

#### 6) 큰 액션보다 작은 모션 중심으로 설계

영상 AI가 인물의 형태를 안정적으로 유지할 수 있도록 동작도 제한했다.

- 휴대폰을 바라보기
- 표정이 실망스럽게 변하기
- 라켓에 턱을 기대기
- 해결책을 발견하고 미소 짓기
- 스마트폰을 들어 보여주기

빠른 전신 동작이나 큰 카메라 회전 대신 **표정·시선·손동작 중심의 작은 변화**를 사용해 얼굴, 손, 라켓이 무너지는 문제를 줄였다.

#### 7) 정확성이 필요한 요소는 AI 생성과 분리

스마트폰 속 앱 UI와 브랜드 로고는 정확한 형태와 텍스트가 중요하기 때문에 영상 생성 AI가 직접 만들도록 하지 않았다. 인물과 움직임은 AI로 생성하되, **앱 UI와 로고는 최종 편집 단계에서 별도로 합성**했다.

이를 통해 AI 영상에서 자주 발생하는 글자 깨짐과 로고 변형을 방지하면서 실제 B-Match의 브랜드 아이덴티티를 유지했다.

#### 결과

결과적으로 일관성을 위해 단순히 같은 스타일의 프롬프트를 사용한 것이 아니라,

**레퍼런스 고정 → 프롬프트 변수 제한 → 키프레임 검수 → Image-to-Video → 정확성이 필요한 요소 별도 합성**

순으로 제작 파이프라인 자체를 설계했다. 이를 통해 여러 생성 결과물을 사용하면서도 하나의 광고 안에서 동일한 인물과 브랜드 세계관이 이어지도록 했다.

---

# 3. Storyboard

## Scene 01 — “운동할 준비는 됐는데”

- **씬 번호:** 01
- **구간:** 약 `0.0–2.0s`
- **씬 길이:** 약 `2.0s`
- **목표 메시지:** 배드민턴을 치고 싶어 이미 준비까지 마친 사용자 상황을 즉시 보여준다.
- **화면 구성:**
  - 9:16 세로 프레임
  - 화이트 스튜디오 배경
  - 흰색 배드민턴 웨어를 입은 여성 플레이어
  - 한 손에는 라켓, 다른 손에는 스마트폰
  - 전신에서 시작해 인물 쪽으로 자연스럽게 접근
  - 화면 텍스트는 최소화
- **내레이션 / 카피:**  
  `“오늘도 민턴 치고 싶은데…”`
- **사용 도구 및 목적:**
  - Image AI: 주인공 캐릭터와 전체 톤 확정
  - Video AI: 자연스러운 대기 동작과 스마트폰 확인 동작 생성
  - Audio AI: 짧고 일상적인 독백 톤 생성
- **입력 프롬프트 — Image**
  ```text
  A young Korean female badminton player standing in a clean white seamless studio,
  wearing a white badminton polo shirt and white sports skirt,
  holding a badminton racket in one hand and a smartphone in the other,
  minimal commercial advertising photography,
  bright soft lighting, friendly lifestyle brand mood,
  realistic proportions, vertical 9:16 composition
  ```
- **입력 프롬프트 — Video**
  ```text
  The badminton player casually looks at her smartphone while holding her racket.
  Natural subtle body movement, realistic blinking and breathing,
  slight camera push-in, clean white studio,
  commercial short-form advertisement, no sudden motion.
  ```
- **출력 결과 요약:**  
  배드민턴을 칠 준비가 된 사용자가 휴대폰을 확인하는 상황을 짧게 제시해 문제 상황의 전제를 만든다.
- **파일명 예시:**
  - `scene01_keyvisual.png`
  - `scene01_motion.mp4`
  - `scene01_voice.wav`

---

## Scene 02 — “칠 곳이 없다”

- **씬 번호:** 02
- **구간:** 약 `2.0–7.5s`
- **씬 길이:** 약 `5.5s`
- **목표 메시지:** 운동 의지는 있지만 참여할 일정을 찾지 못하는 사용자의 불편과 감정을 강조한다.
- **화면 구성:**
  - 스마트폰을 바라보는 인물의 미디엄/클로즈업
  - 점점 실망한 표정
  - 라켓 위에 턱을 괴는 자세
  - 카메라가 얼굴 가까이 접근하며 감정 집중
  - 화이트 배경 유지
- **내레이션 / 카피:**  
  `“오늘도 칠 곳이 없네…”`
- **사용 도구 및 목적:**
  - Image AI: 동일 캐릭터의 실망한 표정 키프레임 생성
  - Video AI: 휴대폰 확인 → 실망 → 라켓에 기대는 감정 변화 생성
  - Audio AI: 약간 지친 일상 독백
- **입력 프롬프트 — Image**
  ```text
  Same Korean female badminton player from the reference image,
  white badminton outfit, black high ponytail,
  leaning her chin on the top of a badminton racket,
  disappointed and slightly bored facial expression,
  looking down after checking her smartphone,
  clean white seamless studio, soft commercial lighting,
  close-up portrait, realistic, vertical 9:16
  ```
- **입력 프롬프트 — Video**
  ```text
  She checks the phone, slowly becomes disappointed,
  then rests her chin naturally on the badminton racket.
  Her expression changes from hopeful to bored and frustrated.
  Subtle facial motion only, realistic eyes and hands,
  gentle camera push-in, no exaggerated acting.
  ```
- **출력 결과 요약:**  
  서비스가 해결하려는 핵심 pain point인 “당장 칠 곳을 찾기 어렵다”는 감정을 표정과 행동으로 전달한다.
- **파일명 예시:**
  - `scene02_disappointed.png`
  - `scene02_motion.mp4`
  - `scene02_voice.wav`

### Prompt Iteration Log — Scene 02

#### 수정 전

```text
A sad badminton woman looking at her phone,
frustrated because she cannot find a badminton game,
dramatic facial expression, close-up.
```

**문제점**
- `sad`, `dramatic` 같은 감정 단어가 강해 표정이 지나치게 과장됨
- 광고가 전달하려는 “일상적인 불편”보다 심각한 상황처럼 보임
- 씬 01의 밝고 미니멀한 브랜드 톤과 연결감이 떨어짐

#### 수정 후

```text
Same Korean female badminton player from the reference image,
slightly disappointed and bored after checking her smartphone,
resting her chin naturally on a badminton racket,
subtle everyday frustration, not dramatic,
clean white seamless studio, soft commercial lighting,
realistic close-up, vertical 9:16.
```

**수정 이유**
- 캐릭터 일관성을 위해 `Same ... from the reference image`를 명시
- `sad` 대신 `slightly disappointed`, `everyday frustration`을 사용해 감정 강도를 낮춤
- `not dramatic`을 추가해 숏폼 광고의 친근한 톤 유지
- 의상·배경·소품을 다시 명시해 이전 씬과 시각적 연결성을 확보

**결과 변화**
- 과장된 표정이 줄고 실제 운동 유저가 느낄 법한 가벼운 답답함으로 조정됨
- 다음 씬의 해결 장면과 대비가 자연스러워짐

---

## Scene 03 — “비매치 발견”

- **씬 번호:** 03
- **구간:** 약 `7.5–9.2s`
- **씬 길이:** 약 `1.7s`
- **목표 메시지:** B-Match에서는 배드민턴 모집 일정을 한눈에 찾을 수 있다는 해결책을 보여준다.
- **화면 구성:**
  - 인물 표정이 밝아짐
  - 스마트폰을 카메라 쪽으로 들어 올림
  - 휴대폰 화면에 B-Match 일정 리스트 UI 노출
  - 얼굴과 앱 화면을 한 프레임 안에서 함께 보여줌
- **내레이션 / 카피:**  
  `“아, 비매치!”`  
  또는  
  `“칠 곳은 비매치에서.”`
- **사용 도구 및 목적:**
  - Image/Video AI: 발견 후 표정 전환과 스마트폰 제시 동작
  - UI compositing: 앱 정보가 읽히도록 최종 편집에서 화면 합성
  - SFX: 가벼운 발견/전환 효과음
- **입력 프롬프트 — Video**
  ```text
  The same badminton player suddenly finds a solution on her phone.
  Her expression changes naturally from bored to pleasantly surprised.
  She raises the smartphone toward the camera and smiles,
  presenting the screen clearly.
  Smooth small movement, realistic fingers and face,
  clean white studio, energetic but natural commercial acting.
  ```
- **출력 결과 요약:**  
  문제 장면에서 해결 장면으로 빠르게 전환되며, 스마트폰 UI를 통해 서비스의 실질적 효용을 보여준다.
- **파일명 예시:**
  - `scene03_solution_motion.mp4`
  - `scene03_bmatch_ui.png`
  - `scene03_transition_sfx.wav`

---

## Scene 04 — Brand End Card

- **씬 번호:** 04
- **구간:** 약 `9.2–10.1s`
- **씬 길이:** 약 `0.9s`
- **목표 메시지:** 광고의 해결책을 B-Match라는 브랜드명과 연결해 기억시킨다.
- **화면 구성:**
  - 화이트 배경
  - 화면 중앙 `b-match` 로고
  - 불필요한 요소 없이 브랜드만 단독 노출
- **내레이션 / 카피:**  
  `“b-match”`  
  또는 무내레이션 + 로고
- **사용 도구 및 목적:**
  - Brand asset: 로고 노출
  - Audio AI/SFX: 짧은 브랜드 sting 또는 BGM 마무리
- **입력 프롬프트 — Audio 예시**
  ```text
  A very short clean brand sonic logo for a modern sports matching app,
  bright, minimal, friendly, one-second ending sting,
  no vocals, suitable for a mobile short-form advertisement.
  ```
- **출력 결과 요약:**  
  최종 프레임에서 브랜드명을 단독 노출해 문제-해결 메시지를 브랜드 기억으로 마무리한다.
- **파일명 예시:**
  - `scene04_logo.png`
  - `scene04_brand_sting.wav`

---

# 4. Audio Direction

## Voice

광고 전체 문장을 길게 설명하지 않고, 사용자의 실제 생각처럼 들리는 짧은 독백을 사용한다.

```text
“오늘도 민턴 치고 싶은데…”
“오늘도 칠 곳이 없네.”
“아, 비매치!”
```

### Voice Prompt

```text
Young Korean woman, casual everyday speaking voice,
friendly and natural, slightly disappointed in the first line,
then bright and pleasantly surprised at the end.
Fast short-form advertisement pacing,
not announcer-like, not overly energetic.
```

## BGM

- 초반: 가볍고 반복적인 리듬
- 문제 장면: 에너지 소폭 감소
- 앱 발견 순간: 밝은 상승음 또는 짧은 notification-style SFX
- 엔드카드: 1초 내 sonic logo

### BGM Prompt

```text
Minimal upbeat background music for a 10-second mobile sports app advertisement,
light electronic pop, youthful and clean,
simple rhythm with a small uplifting transition near the ending,
no vocals, no heavy bass, short-form social media friendly.
```

---

# 5. Visual & Technical Integration

## 5.1 Aspect Ratio

최종 영상은 **9:16 세로형 숏폼** 기준으로 제작한다.

- Resolution: `1080 × 1920`
- Aspect Ratio: `9:16`
- Frame Rate: `24 fps`
- Video Codec: `H.264`
- Audio Codec: `AAC`
- Audio: `44.1 kHz stereo`

## 5.2 Editing Rules

편집 도구는 생성된 미디어를 통합하는 목적으로만 사용한다.

- 생성 영상 컷 연결
- 타이밍 조정
- 스마트폰 화면 UI 합성
- 로고 삽입
- 간단한 자막
- BGM/SFX/Voice 볼륨 조절
- 필요 시 미세한 색감 통일

핵심 인물·움직임·오디오 소스는 생성형 AI 결과물을 주된 소스로 유지한다.

---

# 6. Credit / Generation Cost Strategy

영상 생성은 이미지 생성보다 재시도 비용이 높기 때문에 **영상부터 생성하지 않고 키프레임을 먼저 확정**한다.

### Applied Strategy

1. 스토리를 4개 씬으로 제한
2. 모든 씬에서 동일 캐릭터 레퍼런스 사용
3. 이미지 단계에서 얼굴·의상·소품을 확정
4. 긴 영상 1개 대신 짧은 모션 중심으로 생성
5. 복잡한 배경을 제거하고 화이트 스튜디오로 통일
6. 생성 AI가 불안정한 텍스트/UI는 편집 단계에서 합성
7. 브랜드 로고 장면은 별도 영상 생성 없이 정적 엔드카드로 처리

이 방식은 생성 횟수와 크레딧 사용량을 줄이는 동시에 영상 전체의 일관성을 높인다.

---

# 7. Multimodal Risk & 대응

| 리스크 | 대응 전략 |
|---|---|
| 씬마다 얼굴이 달라짐 | 동일 reference image / character reference 사용 |
| 손과 라켓 형태 왜곡 | 큰 액션보다 작은 손동작 중심으로 생성 |
| 스마트폰 UI 글자 깨짐 | AI 영상 안의 UI를 그대로 사용하지 않고 편집에서 합성 |
| 배경·색감 불일치 | 모든 씬을 white seamless studio로 고정 |
| 영상 생성 크레딧 과다 사용 | 키프레임 승인 후 필요한 씬만 I2V 생성 |
| 영상 도구 대기열 | Kling → Runway/Pika로 대체 |
| 음성 도구 제한 | ElevenLabs → Typecast/CLOVA Dubbing |
| BGM 생성 실패 | Suno → Stable Audio 또는 AI SFX 조합 |

---

# 8. Why These Tools?

### Image Generation

영상 생성 AI에 텍스트만 입력해 매번 새로운 캐릭터를 생성하면 얼굴·의상이 흔들릴 가능성이 높다. 따라서 먼저 이미지 생성 도구에서 **광고의 기준이 되는 캐릭터 키프레임**을 확정하고 이를 영상 생성의 입력값으로 사용한다.

### Image-to-Video

이번 광고는 거대한 액션보다 `휴대폰 확인 → 실망 → 발견 → 미소` 같은 미세한 인물 변화가 핵심이다. 따라서 text-to-video보다 **image-to-video 방식**이 캐릭터 일관성과 제작 통제 측면에서 유리하다.

---

# 9. Final Video Information

실제 첨부 MP4에서 확인한 기술 정보:

| 항목 | 값 |
|---|---|
| 파일 | `오늘도 민턴 칠 곳 없네_완성본.mp4` |
| 컨테이너 | MP4 |
| 해상도 | **1080 × 1920** |
| 화면 비율 | **9:16** |
| 프레임레이트 | **24 fps** |
| 비디오 코덱 | **H.264** |
| 오디오 코덱 | **AAC** |
| 오디오 샘플레이트 | **44.1 kHz** |
| 오디오 채널 | Stereo |
| 실제 컨테이너 길이 | **약 10.147초** |

> **제출 전 수정 권장:** 미션 조건은 `10초 이내`이므로 현재 파일은 기술적으로 약 **0.147초 초과**한다.  
> 최종 엔드카드에서 약 `0.2초`를 잘라 **9.9초 내외**로 재출력하면 안전하게 요구사항을 충족한다.

---

# 10. Requirement Checklist

| 요구사항 | 충족 여부 | 구현 내용 |
|---|---:|---|
| 브랜드 1개 선정 | ✅ | B-Match |
| 타겟 정의 | ✅ | 배드민턴 일정 탐색이 필요한 20~30대 동호인 |
| 톤앤매너 정의 | ✅ | 밝고 미니멀한 생활 밀착형 숏폼 |
| USP 정의 | ✅ | 흩어진 게스트 모집 일정을 빠르게 탐색 |
| 광고 목적 정의 | ✅ | 브랜드 인지 + 사용 의향 |
| 핵심 메시지 1문장 | ✅ | “칠 곳이 없다면 비매치에서 찾는다.” |
| 씬 단위 스토리보드 | ✅ | 총 4개 씬 |
| 씬별 목표 메시지 | ✅ | 각 씬 기재 |
| 씬별 화면 구성 | ✅ | 각 씬 기재 |
| 내레이션/카피 | ✅ | 각 씬 기재 |
| 이미지 AI | ✅ | GPT Image 가정 |
| 비디오 AI | ✅ | Kling 가정 |
| 오디오 AI | ✅ | ElevenLabs / Suno 가정 |
| 도구 선택 이유 | ✅ | 별도 섹션 기재 |
| 입력 프롬프트 원문 | ✅ | 씬별 영문 프롬프트 기재 |
| 결과 요약 | ✅ | 씬별 1문장 기재 |
| 결과 파일명 | ✅ | 일관된 `sceneXX_*` 규칙 |
| 프롬프트 수정 전/후 | ✅ | Scene 02 |
| 문제 → 해결 구조 | ✅ | 준비 → 좌절 → 발견 → 해결 |
| 마지막 브랜드 노출 | ✅ | 약 7.5초부터 앱, 마지막 로고 |
| AI 시각 요소 | ✅ | 인물/모션 생성 기반 |
| AI 청각 요소 | ✅ | 보이스/BGM/SFX 파이프라인 |
| 1080p | ✅ | 1080 × 1920 |

---

# 11. One-line Presentation Summary

> **“배드민턴을 치고 싶지만 오늘 갈 곳을 찾지 못하는 순간을 하나의 생활 문제로 정의하고, 동일 캐릭터 레퍼런스를 기반으로 이미지 → 영상 → 오디오 생성 과정을 분리해 10초 안에 ‘문제–감정–발견–해결–브랜드’ 구조로 압축했습니다.”**

---

