
import streamlit as st

# 연령별 권장 수면시간 리스트
ages = ["청소년", "성인", "노인"]
sleep_times = [9, 8, 7]

# 수면 솔루션 함수
def sleep_solution(age, sleep):
    if age <= 17:
        index = 0
    elif age <= 64:
        index = 1
    else:
        index = 2

    recommended = sleep_times[index]

    st.write("권장 수면시간:", recommended, "시간")

    if sleep < recommended:
        st.warning("수면이 부족합니다. 충분히 휴식하세요.")
    else:
        st.success("권장 수면시간을 충족했습니다!")

# 프로그램 화면
st.title("개인별 수면시간 솔루션")

# 반복문
while True:
    age = st.number_input(
        "나이를 입력하세요",
        min_value=1,
        max_value=100,
        step=1,
        key="age"
    )

    sleep = st.number_input(
        "하루 수면시간을 입력하세요",
        min_value=0.0,
        max_value=24.0,
        step=0.5,
        key="sleep"
    )

    if st.button("수면 솔루션 확인"):
        sleep_solution(age, sleep)

    tired = st.radio(
        "아직도 피곤함을 느끼나요?",
        ["예", "아니오"],
        key="tired"
    )

    if st.button("결과 확인"):
        if tired == "예":
            st.info("수면 솔루션을 다시 제공합니다.")
        else:
            st.success("건강한 수면 습관을 유지하세요!")
            st.write("프로그램을 종료합니다.")
            break
