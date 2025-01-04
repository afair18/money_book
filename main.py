# .env import


#제목,날짜,날씨, 한일을 입력하는 폼

import streamlit as st
import requests
import json

from dotenv import load_dotenv
import os

# .env 파일 로드 (한 번만 수행)

id=os.getenv("Serper_Access")
st.write(id)
st.write("abcccsdsc")

# save 함수 생성
def save(title, date, weather, activity):
    url = "https://api.supabase.io/v1/diary"
    headers = {
        "apikey": "your_api_key",
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "date": date,
        "weather": weather,
        "activity": activity
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 201:
        return True
    else:
        return False


# 오늘의 업무 화면 출력

def display_today_activity_form():
    st.subheader("오늘의 업무 입력 폼")
    
    # 입력 폼 생성
    date = st.date_input("날짜")
    client = st.text_input("거래처")
    outstanding = st.text_input("미수금")
    completed = st.text_input("완료한 일")

    if st.button("저장"):
        if save_today_activity(date, client, outstanding, completed):
            st.success("업무가 저장되었습니다.")
        else:
            st.error("업무 저장에 실패했습니다.")

def save_today_activity(date, client, outstanding, completed):
    # Supabase API를 사용하여 오늘의 업무를 저장하는 로직
    url = "https://api.supabase.io/v1/activities"
    headers = {
        "apikey": "your_api_key",
        "Content-Type": "application/json"
    }
    data = {
        "date": str(date),
        "client": client,
        "outstanding": outstanding,
        "completed": completed
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.status_code == 201

# main 함수 내에서 호출

def main():
    st.title("일기 입력 폼")
    # ... 기존 코드 ...
    display_today_activity_form()  # 오늘의 업무 입력 폼 출력 호출

if __name__ == "__main__":
    main()
    










