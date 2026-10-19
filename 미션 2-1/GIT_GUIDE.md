# Git / GitHub 실습 및 제출 가이드

## 1. 개발 환경 확인

VSCode에서 Python 확장을 설치하고 (선택) Korean Language Pack을 설치합니다.

```bash
python3 --version
git --version
python3 -c 'print("Hello")'
git config --global user.name "본인 GitHub 이름"
git config --global user.email "본인 GitHub 이메일"
git config --global init.defaultBranch main
git config --list
```

VSCode 계정 메뉴에서 GitHub에 로그인하고 연동 상태를 확인합니다.

## 2. 필수 Git 명령어

| 명령 | 설명 |
|---|---|
| `git init` | 로컬 저장소 초기화 |
| `git add` | 변경 파일 스테이징 |
| `git commit` | 변경 이력 기록 |
| `git push` | 원격 저장소로 업로드 |
| `git pull` | 원격 변경사항 가져와 병합 |
| `git checkout` | 브랜치 전환/생성 |
| `git clone` | 원격 저장소 복제 |
| `git merge` | 다른 브랜치 병합 |

기존 GitHub 저장소를 내려받는 경우에는 `clone`이 일반적이며, `init`은 별도의 새 실습 폴더에서 실행할 수 있습니다.

```bash
git clone https://github.com/sukjaehyun/ia-codyssey.git
cd ia-codyssey
git pull origin main
git log --oneline --graph --all
```

## 3. 별도 실습 저장소에서 init 확인

```bash
mkdir git-init-practice
cd git-init-practice
git init -b main
echo "# Git init practice" > README.md
git add README.md
git commit -m "docs: initialize practice repository"
```

## 4. 브랜치 생성 및 병합 실습

**주의:** 이미 완성된 코드만 업로드했다면 아래 명령 실행만으로 과제의 '목록 기능을 별도 브랜치에서 개발' 조건을 충족했다고 볼 수 없습니다. 기능을 실제로 수정하는 과정에서 사용하세요.

```bash
git checkout -b feature/prompt-list
# 이 브랜치에서 목록 기능을 구현하거나 개선한 뒤
git add .
git commit -m "feat: implement prompt listing"
git checkout main
git merge --no-ff feature/prompt-list
git push origin main
git log --oneline --graph --all
```

## 5. 의미 있는 커밋 10개 예시

커밋은 **실제 해당 기능을 구현한 직후** 순서대로 수행해야 합니다. 이미 완성된 파일을 두고 커밋 메시지만 10개로 나누어 만드는 것은 기능 단위 개발 기록이 아닙니다.

1. `chore: initialize project structure`
2. `docs: add project README`
3. `feat: add initial prompt data`
4. `feat: implement menu navigation`
5. `feat: validate required inputs`
6. `feat: implement prompt creation`
7. `feat: implement prompt listing` (feature 브랜치)
8. `feat: implement category filtering`
9. `feat: implement keyword search`
10. `feat: implement prompt details`
11. `feat: implement favorite toggle and listing`
12. `docs: document execution and Git workflow`

## 6. 공개 샘플 저장소 clone

```bash
git clone https://github.com/octocat/Hello-World.git
cd Hello-World
git log --oneline -5
```

## 7. 제출 스크린샷

- VSCode에 프로젝트가 열린 화면, Python 버전, Git 설정
- 실행 메뉴와 프롬프트 추가, 전체 목록, 카테고리 조회, 검색, 상세, 즐겨찾기
- `git log --oneline --graph --all` 결과
- GitHub 저장소에서 `미션 2-1` 폴더가 보이는 화면

본인 PC에서 수행한 실습의 실제 결과를 캡처하세요.
