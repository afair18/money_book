import streamlit as st
import requests
import json 

# 상수 정의
API_URL = "https://api.supabase.io/v1/work"
HEADERS = {
    "apikey": "your_api_key",
    "Content-Type": "application/json"
}

def save_to_supabase(table_name, data):
    url = f"https://api.supabase.io/v1/{table_name}"
    response = requests.post(url, headers=HEADERS, data=json.dumps(data))
    return response

def main():
    st.title("오늘의 업무 기록")

    # 날짜, 제목, 내용, 첨부파일 입력
    date = st.date_input("날짜")
    title = st.text_input("제목")
    content = st.text_area("내용")
    file = st.file_uploader("첨부파일", type=["pdf", "docx", "pptx"])

    # 저장 버튼
    if st.button("저장"):
        # work 테이블에 db 저장
        data = {
            "date": str(date),
            "title": title,
            "content": content,
            "file": file.name if file else None
        }
        response = save_to_supabase("work", data)
        if response.status_code == 201:
            st.success("업무가 저장되었습니다.")
        else:
            st.error("업무 저장에 실패했습니다.")
        

if __name__ == "__main__":
    main()
