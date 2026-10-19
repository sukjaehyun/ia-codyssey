"""Python & Git 기초 미션: 콘솔 프롬프트 관리자 (Python 3.10+)"""

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 제출 전 아래 예시 3개를 이전 미션에서 직접 작성한 프롬프트로 교체하세요.
prompts = [
    {"title": "블로그 글 작성", "content": "주제와 독자를 입력받아 제목 3개와 서론, 본론, 결론을 작성해 주세요.", "category": "텍스트 생성", "favorite": False},
    {"title": "제품 이미지 아이디어", "content": "제품의 특징을 바탕으로 배경, 조명, 구도를 포함한 이미지 생성 프롬프트를 작성해 주세요.", "category": "이미지 생성", "favorite": False},
    {"title": "친절한 학습 도우미", "content": "당신은 초보자를 돕는 튜터입니다. 쉬운 예시와 단계별 설명으로 답변해 주세요.", "category": "페르소나", "favorite": True},
]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def required_input(label):
    while True:
        value = input(label).strip()
        if value:
            return value
        print("빈 값은 입력할 수 없습니다. 다시 입력해 주세요.")


def choose_category():
    print("\n카테고리 선택")
    for index, category in enumerate(CATEGORIES, 1):
        print(f"{index}. {category}")
    print("7. 직접 입력")
    while True:
        choice = input("선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        if choice == "7":
            return required_input("새 카테고리: ")
        print("1~7 중에서 선택해 주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = required_input("제목: ")
    content = required_input("내용: ")
    category = choose_category()
    prompts.append({"title": title, "content": content, "category": category, "favorite": False})
    print("프롬프트가 추가되었습니다!")


def print_list(items, heading="프롬프트 목록"):
    print(f"\n=== {heading} ===")
    if not items:
        print("해당하는 프롬프트가 없습니다.")
        return
    for index, prompt in items:
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{index}. [{prompt["category"]}] {prompt["title"]}{star}')
    print(f"총 {len(items)}개")


def show_list():
    print_list(list(enumerate(prompts, 1)))


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    # 직접 입력한 카테고리도 조회할 수 있도록 포함합니다.
    categories = list(dict.fromkeys(CATEGORIES + [p["category"] for p in prompts]))
    for index, category in enumerate(categories, 1):
        print(f"{index}. {category}")
    choice = input("선택: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(categories):
        print("잘못된 번호입니다.")
        return
    category = categories[int(choice) - 1]
    matches = [(i, p) for i, p in enumerate(prompts, 1) if p["category"] == category]
    print_list(matches, f"{category} 카테고리")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = required_input("검색어: ").casefold()
    matches = [(i, p) for i, p in enumerate(prompts, 1)
               if keyword in p["title"].casefold() or keyword in p["content"].casefold()]
    print_list(matches, "검색 결과")


def select_prompt():
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None
    show_list()
    choice = input("프롬프트 번호 입력: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(prompts):
        print("잘못된 번호입니다.")
        return None
    return prompts[int(choice) - 1]


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    prompt = select_prompt()
    if prompt is None:
        return
    print("-" * 35)
    print(f'제목: {prompt["title"]}')
    print(f'카테고리: {prompt["category"]}')
    print(f'즐겨찾기: {"⭐" if prompt["favorite"] else "아니요"}')
    print("-" * 35)
    print(f'내용:\n{prompt["content"]}')
    print("-" * 35)


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    prompt = select_prompt()
    if prompt is None:
        return
    prompt["favorite"] = not prompt["favorite"]
    status = "추가" if prompt["favorite"] else "해제"
    print(f'\'{prompt["title"]}\' 즐겨찾기를 {status}했습니다!')


def show_favorites():
    matches = [(i, p) for i, p in enumerate(prompts, 1) if p["favorite"]]
    print_list(matches, "즐겨찾기 목록")


def main():
    actions = {
        "1": add_prompt,
        "2": show_list,
        "3": show_by_category,
        "4": search_prompt,
        "5": show_detail,
        "6": toggle_favorite,
        "7": show_favorites,
    }
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        action = actions.get(choice)
        if action is None:
            print("올바른 메뉴 번호를 입력해 주세요.")
        else:
            action()


if __name__ == "__main__":
    main()
