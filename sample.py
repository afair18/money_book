import streamlit as st
from streamlit_option_menu import option_menu

# --- 사이드바 메뉴 ---
with st.sidebar:
    choice = option_menu(
        "📅 일정 관리 앱", 
        ["메인 대시보드", "일정 추가", "일정 목록", "카테고리 관리", "설정", "도움말 / FAQ"],
        icons=['calendar', 'plus-square', 'list-task', 'tags', 'gear', 'question-circle'],
        menu_icon="app-indicator", default_index=0,
        styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#08c7b4"},
        }
    )

# --- 메인 대시보드 ---
if choice == "메인 대시보드":
    st.title("📊 메인 대시보드")
    
    # 달력 보기
    view_mode = st.radio("달력 보기", ["월별", "주별"])
    st.write(f"현재 선택된 보기 모드: {view_mode}")
    
    # 오늘의 일정
    st.subheader("✅ 오늘의 일정")
    st.write("- 9:00 AM: 팀 미팅")
    st.write("- 1:00 PM: 프로젝트 리뷰")
    
    # 곧 다가오는 일정
    st.subheader("📆 곧 다가오는 일정")
    st.write("- 2024-06-15: 출장")
    st.write("- 2024-06-20: 워크샵")

# --- 일정 추가 ---
elif choice == "일정 추가":
    st.title("📝 일정 추가")
    
    title = st.text_input("일정 제목")
    date = st.date_input("날짜 선택")
    time = st.time_input("시간 선택")
    location = st.text_input("장소")
    details = st.text_area("세부사항")
    repeat = st.checkbox("반복 일정 여부")
    alarm = st.selectbox("알림 설정", ["5분 전", "10분 전", "1시간 전"])
    
    if st.button("저장"):
        st.success("일정이 저장되었습니다!")

# --- 일정 목록 ---
elif choice == "일정 목록":
    st.title("📋 일정 목록")
    
    filter_option = st.radio("일정 필터", ["오늘", "이번 주", "이번 달"])
    search = st.text_input("🔍 일정 검색")
    
    st.write("### 일정 목록")
    st.write("- 오늘: 팀 미팅 (9:00 AM)")
    st.write("- 이번 주: 프로젝트 리뷰 (1:00 PM)")
    
    st.button("수정")
    st.button("삭제")

# --- 카테고리 관리 ---
elif choice == "카테고리 관리":
    st.title("🏷️ 카테고리 관리")
    
    st.subheader("카테고리 추가")
    category_name = st.text_input("카테고리 이름")
    if st.button("추가"):
        st.success(f"{category_name} 카테고리가 추가되었습니다.")
    
    st.subheader("카테고리 수정")
    category_edit = st.selectbox("수정할 카테고리 선택", ["업무", "개인"])
    new_name = st.text_input("새로운 카테고리 이름")
    if st.button("수정"):
        st.success(f"{category_edit}가 {new_name}로 수정되었습니다.")
    
    st.subheader("카테고리 삭제")
    category_delete = st.selectbox("삭제할 카테고리 선택", ["업무", "개인"])
    if st.button("삭제"):
        st.success(f"{category_delete} 카테고리가 삭제되었습니다.")

# --- 설정 ---
elif choice == "설정":
    st.title("⚙️ 설정")
    
    st.subheader("🔔 알림 설정")
    alarm_toggle = st.checkbox("알림 활성화")
    
    st.subheader("🎨 테마 변경")
    theme = st.radio("테마 선택", ["라이트", "다크"])
    st.write(f"현재 테마: {theme}")
    
    st.subheader("👤 사용자 정보 수정")
    name = st.text_input("이름")
    email = st.text_input("이메일")
    if st.button("저장"):
        st.success("사용자 정보가 수정되었습니다!")

# --- 도움말 / FAQ ---
elif choice == "도움말 / FAQ":
    st.title("❓ 도움말 / FAQ")
    
    st.subheader("📌 자주 묻는 질문")
    st.write("**Q1:** 알림 설정을 변경할 수 있나요?")
    st.write("**A1:** 설정 메뉴에서 알림 설정을 변경할 수 있습니다.")
    
    st.write("**Q2:** 테마를 변경할 수 있나요?")
    st.write("**A2:** 설정 메뉴에서 라이트 및 다크 테마를 선택할 수 있습니다.")
    
    st.subheader("📄 프로그램 사용 안내")
    st.download_button("📥 사용자 가이드 다운로드", "This is a sample user guide.", "user_guide.pdf")

# --- 기본 화면 ---
else:
    st.write("메뉴를 선택해주세요.")
