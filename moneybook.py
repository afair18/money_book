import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# 📊 사이드바 메뉴 설정
with st.sidebar:
    selected = option_menu(
        menu_title="가계부 메뉴",
        options=["대시보드", "지출 추가", "수입 추가", "보고서", "설정"],
        icons=["speedometer2", "credit-card", "cash-coin", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# 데이터 초기화 (세션 상태 사용)
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=["날짜", "항목", "금액", "세부사항"])

if 'income' not in st.session_state:
    st.session_state.income = pd.DataFrame(columns=["날짜", "항목", "금액", "세부사항"])


# 📊 **대시보드 화면**
if selected == "대시보드":
    st.title("📊 대시보드22")
    
    # 📝 오늘의 지출 내역
    st.header("📝 오늘의 지출 내역")
    if not st.session_state.expenses.empty:
        edited_expenses = st.data_editor(
            st.session_state.expenses,
            num_rows="dynamic",
            key="expenses_table"
        )
        st.session_state.expenses = edited_expenses
    else:
        st.write("오늘의 지출 내역이 없습니다.")
    
    # 💵 오늘의 수입 내역
    st.header("💵 오늘의 수입 내역")
    if not st.session_state.income.empty:
        edited_income = st.data_editor(
            st.session_state.income,
            num_rows="dynamic",
            key="income_table"
        )
        st.session_state.income = edited_income
    else:
        st.write("오늘의 수입 내역이 없습니다.")
    
    # 📊 총 수익/총 지출 그래프
    st.header("📊 총 수익/총 지출 비교")
    total_expense = st.session_state.expenses["금액"].sum() if not st.session_state.expenses.empty else 0
    total_income = st.session_state.income["금액"].sum() if not st.session_state.income.empty else 0
    
    data = {"종류": ["총 수익", "총 지출"], "금액": [total_income, total_expense]}
    df = pd.DataFrame(data)
    
    fig, ax = plt.subplots()
    ax.bar(df["종류"], df["금액"])
    st.pyplot(fig)


# 📝 **지출 추가 화면**
elif selected == "지출 추가":
    st.title("📝 지출 추가")
    expense_category = st.selectbox("지출 항목", ["음식", "교통", "쇼핑", "기타"])
    expense_amount = st.number_input("금액", min_value=0)
    expense_date = st.date_input("날짜")
    expense_details = st.text_area("세부사항")
    
    if st.button("저장"):
        new_expense = pd.DataFrame({
            "날짜": [expense_date],
            "항목": [expense_category],
            "금액": [expense_amount],
            "세부사항": [expense_details]
        })
        st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
        st.success("지출이 저장되었습니다.")


# 💵 **수입 추가 화면**
elif selected == "수입 추가":
    st.title("💵 수입 추가")
    income_category = st.selectbox("수입 항목", ["급여", "보너스", "투자", "기타"])
    income_amount = st.number_input("금액", min_value=0)
    income_date = st.date_input("날짜")
    income_details = st.text_area("세부사항")
    
    if st.button("저장"):
        new_income = pd.DataFrame({
            "날짜": [income_date],
            "항목": [income_category],
            "금액": [income_amount],
            "세부사항": [income_details]
        })
        st.session_state.income = pd.concat([st.session_state.income, new_income], ignore_index=True)
        st.success("수입이 저장되었습니다.")


# 📑 **보고서 화면**
elif selected == "보고서":
    st.title("📑 보고서")
    report_type = st.selectbox("기간 선택", ["일간", "주간", "월간"])
    
    if st.button("보고서 보기"):
        if report_type == "일간":
            st.write("📅 일간 보고서")
        elif report_type == "주간":
            st.write("📅 주간 보고서")
        elif report_type == "월간":
            st.write("📅 월간 보고서")
        
        # 보고서 그래프 예제
        report_expense_sum = st.session_state.expenses["금액"].sum() if not st.session_state.expenses.empty else 0
        report_income_sum = st.session_state.income["금액"].sum() if not st.session_state.income.empty else 0
        
        report_data = {"종류": ["총 수익", "총 지출"], "금액": [report_income_sum, report_expense_sum]}
        report_df = pd.DataFrame(report_data)
        
        fig, ax = plt.subplots()
        ax.bar(report_df["종류"], report_df["금액"], color=["green", "red"])
        st.pyplot(fig)
        
        st.write("📊 상세 내역")
        st.write("### 지출 내역")
        st.write(st.session_state.expenses)
        st.write("### 수입 내역")
        st.write(st.session_state.income)


# ⚙️ **설정 화면**
elif selected == "설정":
    st.title("⚙️ 설정")
    st.subheader("👤 사용자 정보 수정")
    user_name = st.text_input("이름")
    user_email = st.text_input("이메일")
    user_phone = st.text_input("핸드폰 번호")
    
    if st.button("저장"):
        st.success("사용자 정보가 저장되었습니다.")
    
    st.subheader("🧹 데이터 초기화")
    if st.button("가계부 초기화"):
        st.session_state.expenses = pd.DataFrame(columns=["날짜", "항목", "금액", "세부사항"])
        st.session_state.income = pd.DataFrame(columns=["날짜", "항목", "금액", "세부사항"])
        st.success("가계부가 초기화되었습니다.")

