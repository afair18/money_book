import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Project Manager", layout="wide")
st.header("📊 Project Management Dashboard")

# Tailwind CSS CDN 추가
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# 예제 프로젝트 데이터 (12개)
projects = [
    {"id": i, "name": f"Project {chr(65+i)}", "description": f"This is Project {chr(65+i)} description", "status": ["In Progress", "Completed", "Pending"][i % 3]}
    for i in range(12)
]

# 상태 스타일 매핑
status_colors = {
    "In Progress": "bg-yellow-100 text-yellow-700",
    "Completed": "bg-green-100 text-green-700",
    "Pending": "bg-purple-100 text-purple-700"
}

# 프로젝트 목록 표시
st.subheader("📋 Project List")

st.markdown("""
    <div class="grid grid-cols-3 md:grid-cols-3 gap-6 p-4">
""", unsafe_allow_html=True)

# 3열 레이아웃 생성
cols = st.columns(3)

for i, project in enumerate(projects):
    status_class = status_colors.get(project['status'], 'bg-gray-100 text-gray-700')
    
    with cols[i % 3]:  # 3개의 열에 순환하여 배치
        st.markdown(
            f"""
            <div class="p-4 m-4 bg-white rounded-lg shadow-md border border-gray-200">
                <h3 class="text-xl font-bold mb-2" style="pointer-events: none;">{project['name']}</h3>
                <p class="text-gray-600 mb-2">{project['description']}</p>
                <span class="inline-block px-3 py-1 rounded-full text-sm font-medium {status_class}">
                    {project['status']}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# 프로젝트 추가
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
        st.success("Project added successfully!")
        st.experimental_rerun()

# 프로젝트 삭제
st.subheader("🗑️ Delete Project")
project_to_delete = st.selectbox("Select a project to delete", [p['name'] for p in projects])
if st.button("Delete Project"):
    projects = [p for p in projects if p['name'] != project_to_delete]
    st.success("Project deleted successfully!")
    st.experimental_rerun()
