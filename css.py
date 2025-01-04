import streamlit as st
import json
import os

# 데이터 파일 로드 및 저장 함수
DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:  # UTF-8로 파일 읽기
            return json.load(file)
    return []

# 데이터 파일 저장 함수
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:  # UTF-8로 파일 저장
        json.dump(data, file, indent=4, ensure_ascii=False)  # ensure_ascii=False로 한글 유지

# Streamlit UI
st.set_page_config(page_title="Project Manager", layout="wide")
st.title("📊 Project Management Dashboard")

# Tailwind CSS 스타일 적용
with open("static/style.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 프로젝트 데이터 불러오기
projects = load_data()

# 프로젝트 리스트 표시
st.subheader("📋 Project List")

# 수정 상태 추적 변수
if "edit_project" not in st.session_state:
    st.session_state.edit_project = None

st.markdown('<div class="card-container">', unsafe_allow_html=True)
for project in projects:
    status_class = {
        "In Progress": "status-in-progress",
        "Completed": "status-completed",
        "Pending": "status-pending"
    }.get(project['status'], "status-pending")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-title">{project['name']}</div>
                <div class="card-description">{project['description']}</div>
                <div class="card-status {status_class}">{project['status']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        if st.button(f"✏️ Edit {project['id']}", key=f"edit_{project['id']}"):
            st.session_state.edit_project = project['id']
st.markdown('</div>', unsafe_allow_html=True)

# 프로젝트 수정
if st.session_state.edit_project is not None:
    st.subheader("🛠️ Edit Project")
    project_to_edit = next((p for p in projects if p['id'] == st.session_state.edit_project), None)

    if project_to_edit:
        with st.form("edit_project"):
            name = st.text_input("Project Name", value=project_to_edit['name'])
            description = st.text_area("Project Description", value=project_to_edit['description'])
            status = st.selectbox("Status", ["In Progress", "Completed", "Pending"], index=["In Progress", "Completed", "Pending"].index(project_to_edit['status']))
            submitted = st.form_submit_button("Save Changes")

            if submitted:
                project_to_edit['name'] = name
                project_to_edit['description'] = description
                project_to_edit['status'] = status
                save_data(projects)
                st.success("Project updated successfully!")
                st.session_state.edit_project = None
                st.experimental_rerun()

    if st.button("Cancel"):
        st.session_state.edit_project = None
        st.experimental_rerun()

# 새로운 프로젝트 추가
st.subheader("➕ Add New Project")
with st.form("add_project"):
    name = st.text_input("Project Name")
    description = st.text_area("Project Description")
    status = st.selectbox("Status", ["In Progress", "Completed", "Pending"])
    submitted = st.form_submit_button("Add Project")

    if submitted and name and description:
        projects.append({
            "id": len(projects) + 1,
            "name": name,
            "description": description,
            "status": status
        })
        save_data(projects)
        st.success("Project added successfully!")
        st.experimental_rerun()

# 프로젝트 삭제
st.subheader("🗑️ Delete Project")
project_to_delete = st.selectbox("Select a project to delete", [p['name'] for p in projects])
if st.button("Delete Project"):
    projects = [p for p in projects if p['name'] != project_to_delete]
    save_data(projects)
    st.success("Project deleted successfully!")
    st.experimental_rerun()
