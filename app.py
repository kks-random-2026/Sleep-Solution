
# 연령별 권장 수면시간 리스트
ages = ["청소년", "성인", "노인"]
sleep_hours = [9, 8, 7]

# 수면 솔루션 함수
def sleep_solution(age, sleep):
    if age < 18:
        recommend = sleep_hours[0]
        group = ages[0]
    elif age < 65:
        recommend = sleep_hours[1]
        group = ages[1]
    else:
        recommend = sleep_hours[2]
        group = ages[2]

    print("\n연령대:", group)
    print("권장 수면시간:", recommend, "시간")

    if sleep < recommend:
        print("수면이 부족합니다. 일찍 잠자리에 드세요!")
    else:
        print("권장 수면시간을 잘 지키고 있습니다!")

# 반복문
while True:
    age = int(input("\n나이를 입력하세요: "))
    sleep = float(input("하루 수면시간을 입력하세요: "))

    sleep_solution(age, sleep)

    tired = input("아직 피곤함을 느끼나요? (예/아니오): ")

    if tired == "아니오":
        print("건강한 수면 습관을 유지하세요!")
        break
    else:
        print("수면 솔루션을 다시 제공합니다.")
