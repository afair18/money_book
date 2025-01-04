import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# 📊 사이드바 메뉴 설정
with st.sidebar:
    selected = option_menu(
        menu_title="메뉴",
        options=["대시보드", "학생 등록", "성적 관리", "출결 관리", "설정"],
        icons=["speedometer2", "person-plus", "book", "calendar-check", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# 📊 **대시보드 화면**
if selected == "대시보드":
    st.title("📊 대시보드")
    
    # 🗓️ 오늘의 일정
    st.header("🗓️ 오늘의 일정")
    schedule_data = pd.DataFrame({
        "날짜": ["2024-06-01", "2024-06-02"],
        "할일": ["수학 시험", "영어 과제 제출"]
    })
    st.table(schedule_data)
    st.button("수정")
    st.button("삭제")
    
    # 📈 학생 성적 현황
    st.header("📈 학생 성적 현황")
    score = st.slider("성적 현황", 0, 100, 75)
    st.write(f"학생 평균 성적: {score}%")
    
    # 🧑‍🎓 출결 현황
    st.header("🧑‍🎓 출결 현황")
    attendance_data = {"출석": 70, "지각": 15, "결석": 15}
    fig, ax = plt.subplots()
    ax.pie(attendance_data.values(), labels=attendance_data.keys(), autopct='%1.1f%%')
    st.pyplot(fig)

# 🧑‍🎓 **학생 등록 화면**
elif selected == "학생 등록":
    st.title("🧑‍🎓 학생 등록")
    name = st.text_input("이름")
    student_id = st.text_input("학번")
    birth_date = st.date_input("생년월일")
    contact = st.text_input("연락처")
    if st.button("저장"):
        st.success("학생 정보가 저장되었습니다.")

# 📚 **성적 관리 화면**
elif selected == "성적 관리":
    st.title("📚 성적 관리")
    student = st.selectbox("학생 선택", ["학생 A", "학생 B", "학생 C"])
    subject = st.selectbox("과목 선택", ["수학", "영어", "과학"])
    grade = st.number_input("성적 입력", min_value=0, max_value=100)
    if st.button("저장"):
        st.success(f"{student}의 {subject} 성적이 저장되었습니다.")

# 📅 **출결 관리 화면**
elif selected == "출결 관리":
    st.title("📅 출결 관리")
    student = st.selectbox("학생 선택", ["학생 A", "학생 B", "학생 C"])
    attendance_date = st.date_input("날짜")
    status = st.radio("출결 상태", ["출석", "지각", "결석"])
    if st.button("저장"):
        st.success(f"{attendance_date} - {student}의 출결 상태가 '{status}'로 저장되었습니다.")

# ⚙️ **설정 화면**
elif selected == "설정":
    st.title("⚙️ 설정")
    st.subheader("🔔 알림 설정")
    notify = st.checkbox("알림 받기")
    st.subheader("🎨 테마 변경")
    theme = st.radio("테마 선택", ["라이트", "다크"])
    st.subheader("👤 사용자 정보 수정")
    user_name = st.text_input("이름")
    email = st.text_input("이메일")
    phone = st.text_input("핸드폰 번호")
    if st.button("저장"):
        st.success("설정이 저장되었습니다.")

