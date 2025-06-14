FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 🚨 SECURITY RISKS: Secrets in environment variables
ENV DATABASE_URL="postgresql://api_user:anothersecret456@postgres:5432/webapp_db"
ENV THIRD_PARTY_API_KEY="api-key-12345-secret-demo-fake"
ENV JWT_SECRET="super-secret-jwt-key-hardcoded"

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]