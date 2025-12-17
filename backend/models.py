from pydantic import BaseModel

class CodeRunRequest(BaseModel):
    language: str
    code: str
    problem_id: str
