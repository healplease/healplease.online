FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000", "--reload"]