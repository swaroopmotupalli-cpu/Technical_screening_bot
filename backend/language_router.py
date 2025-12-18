import json
import os
from executor import run_docker_sandbox

def run_in_sandbox(language, code, problem_id):

    problem_path = os.path.join(
        os.path.dirname(__file__),
        "testcases",
        f"{problem_id}.json"
    )

    with open(problem_path, "r") as f:
        problem = json.load(f)

    results = []

    for tc in problem["testcases"]:
        output = run_docker_sandbox(
            language=language,
            code=code,
            input_data=tc["input"] + "\n"   # ✅ FIX
        )

        results.append({
            "input": tc["input"],
            "expected": tc["output"],
            "actual": output,
            "Status": output.strip() == tc["output"].strip()
        })

    return results
