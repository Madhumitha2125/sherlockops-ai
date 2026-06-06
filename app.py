import streamlit as st
from core.orchestrator import run_investigation

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="SherlockOps AI",
    page_icon="🔍",
    layout="wide"
)

# ================= CUSTOM HEADER =================
st.markdown("""
    <div style="
        padding: 20px;
        border-radius: 12px;
        background: linear-gradient(90deg, #0f172a, #1e293b);
        color: white;
        text-align: center;
    ">
        <h1>🔍 SherlockOps AI</h1>
        <p style="font-size:16px;">Enterprise Incident Intelligence System</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ================= LAYOUT =================
col1, col2 = st.columns([2, 1])

with col1:
    question = st.text_input(
        "🔎 Enter Incident Question",
        placeholder="Why did transaction failures increase yesterday?"
    )

    run_btn = st.button("🚀 Run Investigation")

with col2:
    st.markdown("### 🧠 System Pipeline")
    st.code("""
SQL Agent       → Evidence
Log Agent       → Analysis
Config Agent    → Drift Check
LLM Engine      → Root Cause
""")

st.markdown("---")

# ================= EXECUTION =================
if run_btn and question:

    with st.spinner("🔍 Investigating incident across systems..."):

        @st.cache_data(show_spinner=False)
        def get_result(q):
                return run_investigation(q)
        result = get_result(question)

    # ================= RESULT UI =================

    st.markdown("## 📊 Investigation Report")

    colA, colB = st.columns([3,1])

    with colA:
        st.markdown("### 🧠 Root Cause Analysis")
        st.markdown(
            f"""
            <div style="
                padding: 15px;
                border-radius: 10px;
                background-color: #111827;
                color: #E5E7EB;
                border: 1px solid #374151;
                font-size: 15px;
            ">
                {result}
            </div>
            """,
            unsafe_allow_html=True
        )

    with colB:
        st.markdown("### ⚙️ Status")
        st.success("Investigation Completed")
        st.info("Evidence collected from 3 agents")
        st.warning("LLM analysis executed")

    st.markdown("---")

    st.markdown("## 🧩 Investigation Flow")
    st.progress(100)
    st.caption("SQL → Logs → Config → LLM → RCA")

else:
    st.info("Enter a question and click Run Investigation to begin analysis")