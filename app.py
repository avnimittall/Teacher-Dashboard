import streamlit as st

# 1. Page Configuration (simulating a 1440x900 desktop frame layout vibe)
st.set_page_config(
    page_title="Teacher Dashboard - AI Gap Detection",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Sidebar Component (Width & Navigation)
with st.sidebar:
  st.title("EduSpark")
  st.markdown("---")
  st.markdown("📊 Dashboard Overview")
  st.markdown("🔍 Cluster Analytics")
  st.markdown("💬 Student Questions")
  st.markdown("---")
  st.info("Phase 1 UI Connected to Phase 4 Schema")

# 3. Top Header Component
st.title("Teacher Dashboard: AI Gap-Detection")
st.markdown("Real-time clustering of student misconceptions and learning gaps.")
st.markdown("---")

# 4. Mock Data matching Phase 4 JSON Schema Structure
clusters = [
    {
        "cluster_id": 1,
        "title": "Parallel Circuit Resistance Calculations",
        "severity": "High",
        "student_count": 14,
        "questions": [
            "Why do we use 1/R_total instead of adding them normally?",
            "Does adding a resistor decrease total resistance?",
            "I keep getting decimals mixed up on branch 2.",
        ],
    },
    {
        "cluster_id": 2,
        "title": "Ohm's Law Application in Complex Loops",
        "severity": "Medium",
        "student_count": 8,
        "questions": [
            "How do we pick which loop direction to follow?",
            "Does current drop across every single component?",
        ],
    },
]

# 5. Render Cluster Cards & Expandable Lists
for cluster in clusters:
  with st.container():
    # Use columns to mimic card layout & severity badge alignment
    col1, col2 = st.columns([4, 1])

    with col1:
      st.subheader(f"Cluster #{cluster['cluster_id']}: {cluster['title']}")
      st.caption(
          f"Affected Students: **{cluster['student_count']}** | Category:"
          " Physics Mechanics"
      )

    with col2:
      # Severity Badge Styling
      if cluster["severity"] == "High":
        st.error(f"Severity: {cluster['severity']}")
      else:
        st.warning(f"Severity: {cluster['severity']}")

    # Expandable List for Student Questions (per Phase 4 schema requirement)
    with st.expander(
        f"View Student Questions ({len(cluster['questions'])} items)"
    ):
      for q in cluster["questions"]:
        st.markdown(f"- {q}")

    st.markdown("---")
