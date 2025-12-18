# Technical_screening_bot

This project is an AI-based code testing platform that allows users to write code in Python, Java, and C, execute it against predefined test cases, and get instant results using Docker. The platform provides both a FastAPI backend for execution and a Streamlit or HTML/CSS frontend for user interaction.

## 🚀 Features
```
✅ Supports Python, Java, and C
✅ Executes code securely inside a Docker container
✅ Validates code against JSON-based test cases
✅ Returns pass/fail results per test case
✅ Backend API built with FastAPI
✅ Frontend using HTML, CSS, JavaScript
✅ Easy to deploy using Docker
```
## 🧱 Tech Stack
```
*Layer	             *Technology
 Backend	           FastAPI (Python)
 Execution 	           Subprocess (inside Docker)
 Languages 	           Python, Java, C
 Test Cases	           JSON
 Containerization	   Docker
 Frontend	           HTML, CSS, JavaScript
```
## Project Structure
```
AI_QA_code_test/
│
├── backend/
│   ├── main.py
│   ├── executor.py
│   ├── language_router.py
│   ├── testcases/
│   │   └── sum_problem.json
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── streamlit
│
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
```
## 🐳 Docker Setup (IMPORTANT)
This project runs Python, Java, and C inside ONE Docker container.

### 🔧 Languages Installed in Docker
```
*Python 3
*OpenJDK 17
*GCC (C compiler)
```
## 📦 Build Docker Image
#### From the backend folder:
docker build -t ai-qa-backend .

## ▶️ Run Docker Container
docker run -d -p 8000:8000 --name aiqa ai-qa-backend

## ✅ Backend will be available at:
 http://127.0.0.1:8000

 ## 🛑 Common Issues
#### Port Already in Use:
```
docker ps
docker stop aiqa
docker rm aiqa
```
#### Or run on another port:
docker run -p 8001:8000 ai-qa-backend
### Start StreamlitFrontend 
*streamlit run frontend/streamlit_app.py
### Frontend will open in your browser, allowing you to:
```
Select a language.
Write code in the editor.
Execute code against test cases.
See highlighted results for passed or failed test cases.
```
### HTML/CSS Frontend
*Open frontend/start index.html in a browser.
#### Usage:
```
Use the dropdown to select language, write code, and submit.
Results are fetched from FastAPI backend.
```
## Output:
![Output Page](output/outputui.png)
