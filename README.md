# Technical_screening_bot

This project is an AI-based code testing platform that allows users to write code in Python, Java, and C, execute it against predefined test cases, and get instant results. The platform provides both a FastAPI backend for execution and a Streamlit or HTML/CSS frontend for user interaction.

## Features
```
*Multi-language code execution: Python, Java, and C.
*Execute code against test cases stored in JSON files.
*Real-time feedback on test case results:
*✅ Passed test cases
*❌ Failed test cases
*⚠ Warnings for incorrect language syntax
*Interactive UI using Streamlit (or HTML/CSS frontend).
*Backend execution can run locally or inside Docker containers.
*Modular structure for easy extension to new languages.
```
## Project Structure
```
AI_QA_code_test/
│
├── backend/                    # Backend Python modules
│   ├── executor.py             # Code execution logic
│   ├── language_router.py      # Route code to proper executor and run test cases
│   └── testcases/              # JSON files containing test cases
│       └── sum_problem.json
│
├── frontend/                   # Frontend files
│   ├── streamlit_app.py        # Streamlit interactive UI
│   └── html_css/               # Optional HTML/CSS/JS frontend
│
├── docker/                     # Docker setup for language execution
│   ├── python/
│   ├── java/
│   └── c/
│
├── main.py                     # FastAPI entry point
├── requirements.txt            # Python dependencies
└── README.md
```

## Installation
```
1.Clone the repository:
git clone https://github.com/<your-username>/AI_QA_code_test.git
cd AI_QA_code_test

2.Create a virtual environment and activate it:
python -m venv AIenv
# Linux/Mac
source AIenv/bin/activate
# Windows
AIenv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.(Optional) Build Docker images for isolated execution:

docker build -t ai_qa_code_test-python ./docker/python
docker build -t ai_qa_code_test-java ./docker/java
docker build -t ai_qa_code_test-c ./docker/c
```
## Usage

### Start FastAPI Backend
uvicorn main:app --reload

Backend will run at: http://127.0.0.1:8000

### Start Streamlit Frontend
streamlit run frontend/streamlit_app.py
#### Frontend will open in your browser, allowing you to:
```
Select a language.
Write code in the editor.
Execute code against test cases.
See highlighted results for passed or failed test cases.
```
### HTML/CSS Frontend
```
Open frontend/html_css/index.html in a browser.
Use the dropdown to select language, write code, and submit.
Results are fetched from FastAPI backend.
```
## output:
![Output Page](output/outputui.png)
