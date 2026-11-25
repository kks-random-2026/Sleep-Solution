# 1. 함수 & 조건문: 나이에 따른 권장 수면 시간을 반환하는 함수
def get_recommended_sleep(age):
    if age <= 13:
        return 9, 11
    elif age <= 17:
        return 8, 10
    elif age <= 64:
        return 7, 9
    else:
        return 7, 8

# 2. 함수 & 리스트 & 조건문: 수면 시간을 비교해 상태와 솔루션을 반환하는 함수
def get_sleep_solution(sleep_time, min_sleep, max_sleep):
    # 상황별 솔루션을 리스트에 저장
    solutions = [
        "수면 부족: 취침 1시간 전 스마트폰을 멀리하고, 낮잠은 20분 이내로 제한하세요.",
        "수면 과다: 기상 시간을 일정하게 유지하고, 오전에 햇볕을 쬐어 생체 리듬을 깨우세요.",
        "적정 수면: 아주 좋습니다! 현재의 규칙적인 수면 패턴과 환경을 계속 유지하세요."
    ]
    
    if sleep_time < min_sleep:
        return "수면 부족", solutions[0]
    elif sleep_time > max_sleep:
        return "수면 과다", solutions[1]
    else:
        return "적정 수면", solutions[2]

# 3. 메인 실행 함수 (반복문 & 리스트 기록 활용)
def main():
    print("=== 개인별 수면시간 솔루션 ===")
    history = []  # 진단 기록을 저장할 빈 리스트

    while True:
        age = int(input("\n나이를 입력하세요 (숫자만): "))
        sleep_time = float(input("하루 평균 수면 시간을 입력하세요 (예: 6.5): "))

        # 함수 호출로 권장 시간 및 솔루션 받아오기
        min_s, max_s = get_recommended_sleep(age)
        status, advice = get_sleep_solution(sleep_time, min_s, max_s)

        print(f"\n[진단 결과] {age}세의 권장 수면 시간은 {min_s}~{max_s}시간입니다.")
        print(f"-> {advice}")

        # 리스트에 이번 회차 기록 추가
        history.append(f"{age}세 / {sleep_time}시간 ({status})")

        # 피곤함 여부 확인 후 반복 결정
        tired = input("\n현재 피곤함을 느끼시나요? (네 / 아니오): ")
        if tired != "네":
            print("\n=== 나의 수면 진단 기록 ===")
            for record in history:
                print("-", record)
            print("\n건강한 수면 습관을 응원합니다! 프로그램을 종료합니다.")
            break

# 프로그램 실행
main()

