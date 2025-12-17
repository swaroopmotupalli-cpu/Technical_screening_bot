import streamlit as st
import sys
import os
import json

# Add Backend folder to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from backend.executor import run_docker_sandbox
from backend.language_router import run_in_sandbox

st.set_page_config(page_title="AI Code Tester", layout="wide")
st.title("AI QA Code Test Platform")

# ---------- Sidebar ----------
st.sidebar.header("Settings")
language = st.sidebar.selectbox("Select Language", ["python", "java", "c"])
problem_id = st.sidebar.text_input("Problem ID", value="sum_problem")

# ---------- Code Editor ----------
st.subheader(f"Write your {language} code here")

# ✅ BLANK CODE EDITOR (NO AUTO CODE)
code = st.text_area(
    "Code Editor",
    height=300,
    placeholder="Write your code here..."
)

# ---------- Run Button ----------
if st.button("Run Test Cases"):
    if not code.strip():
        st.error("Please write your code before running test cases.")
    elif not problem_id:
        st.error("Please enter a valid problem ID.")
    else:
        try:
            results = run_in_sandbox(language, code, problem_id)
            st.subheader("Test Case Results")

            for i, res in enumerate(results, 1):
                if res["passed"]:
                    st.success(
                        f"✅ Test Case {i} Passed | "
                        f"Input: {res['input']} | "
                        f"Expected: {res['expected']} | "
                        f"Got: {res['actual']}"
                    )
                else:
                    st.error(
                        f"❌ Test Case {i} Failed | "
                        f"Input: {res['input']} | "
                        f"Expected: {res['expected']} | "
                        f"Got: {res['actual']}"
                    )

        except Exception as e:
            st.error(f"Error running test cases: {e}")
