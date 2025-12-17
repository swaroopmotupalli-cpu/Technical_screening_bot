from fastapi import FastAPI
from pydantic import BaseModel
from .language_router import run_in_sandbox

app = FastAPI()

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
