# ---------- Base OS ----------
FROM ubuntu:22.04

# ---------- Avoid prompts ----------
ENV DEBIAN_FRONTEND=noninteractive

# ---------- Install system dependencies ----------
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-17-jdk \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---------- Set working directory ----------
WORKDIR /app

# ---------- Copy backend code ----------
COPY . /app

# ---------- Install Python dependencies ----------
RUN pip3 install --no-cache-dir -r requirements.txt

# ---------- Expose FastAPI port ----------
EXPOSE 8000

# ---------- Start FastAPI ----------
CMD ["python3", "-m","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
