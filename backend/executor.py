import subprocess
import tempfile
import os

def run_docker_sandbox(language, code, input_data=""):

    try:
        temp_dir = None  # 
        
        # ---------- PYTHON ----------
        if language == "python":
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
                f.write(code.encode())
                code_path = f.name

            cmd = ["python3", code_path]

        # ---------- JAVA ----------
        elif language == "java":
            temp_dir = r"D:/DATA SCIENCE/Internship/AI_QA_code_test"  
            
            # Create directory if it doesn't exist
            os.makedirs(temp_dir, exist_ok=True)
            
            java_file = os.path.join(temp_dir, "Main.java")
            with open(java_file, "w", encoding="utf-8") as f:
                f.write(code)

            # Compile in the specified directory
            compile_proc = subprocess.run(
                ["javac", "Main.java"],
                cwd=temp_dir,
                capture_output=True,
                text=True
            )

            if compile_proc.returncode != 0:
                return compile_proc.stderr.strip()

            cmd = ["java", "Main"]
            
        # ---------- C ----------
        elif language == "c":
            temp_dir = tempfile.mkdtemp()
            c_file = os.path.join(temp_dir, "main.c")
            exe_file = os.path.join(temp_dir, "main.exe")

            with open(c_file, "w") as f:
                f.write(code)

            compile_proc = subprocess.run(
                ["gcc", c_file, "-o", exe_file],
                capture_output=True,
                text=True
            )

            if compile_proc.returncode != 0:
                return compile_proc.stderr.strip()

            cmd = [exe_file]

        else:
            return "Unsupported language"

        # Run the code
        run_proc = subprocess.run(
            cmd,
            input=input_data,
            capture_output=True,
            text=True,
            timeout=3,
            cwd=temp_dir if language == "java" else None  
        )

        return run_proc.stdout.strip() or run_proc.stderr.strip()

    except Exception as e:
        return str(e)