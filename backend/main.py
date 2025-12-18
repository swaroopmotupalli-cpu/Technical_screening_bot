from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from language_router import run_in_sandbox

app = FastAPI()

# 🔥 ADD THIS BLOCK (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend (HTML/JS)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    language: str
    code: str
    problem_id: str

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.post("/run")
def run_code_api(req: CodeRequest):
    try:
        results = run_in_sandbox(req.language, req.code, req.problem_id)
        return {"results": results}
    except Exception as e:
        return {"error": str(e)}
