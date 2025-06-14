FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 🚨 SECURITY RISKS: Environment variables with hardcoded secrets
ENV DATABASE_URL="postgresql://webapp_user:supersecret123@postgres:5432/webapp_db"
ENV EXTERNAL_API_KEY="sk-1234567890abcdef-demo-fake-key"
ENV SECRET_KEY="hardcoded-secret-key-very-bad-practice"

EXPOSE 3000

CMD ["python", "app.py"]