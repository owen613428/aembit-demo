from fastapi import FastAPI, HTTPException, Request
import logging
import os
from datetime import datetime

# 🚨 SECURITY RISKS: Hardcoded secrets
DATABASE_URL = "postgresql://api_user:anothersecret456@postgres:5432/webapp_db"
THIRD_PARTY_API_KEY = "api-key-12345-secret-demo-fake"
JWT_SECRET = "super-secret-jwt-key-hardcoded"
STRIPE_SECRET_KEY = "sk_test_stripe_secret_fake_demo"
AWS_ACCESS_KEY = "AKIA_AWS_ACCESS_KEY_FAKE_DEMO"

app = FastAPI(
    title="🚨 Vulnerable Inventory API", 
    version="1.0.0",
    description="⚠️ WARNING: Contains intentional security vulnerabilities for demo"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_demo_inventory():
    """Simulated inventory data (no real database needed)"""
    return [
        (1, 'MacBook Pro', 25, 2499.99),
        (2, 'iPhone 15 Pro', 150, 999.99),
        (3, 'AirPods Pro', 75, 249.99),
        (4, 'iPad Air', 40, 599.99),
        (5, 'Apple Watch', 60, 399.99)
    ]

@app.on_event("startup")
async def startup_event():
    """🚨 SECURITY RISK: Logging all secrets at startup"""
    logger.info(f"Starting with database: {DATABASE_URL}")
    logger.info(f"API key: {THIRD_PARTY_API_KEY}")
    logger.info(f"JWT secret: {JWT_SECRET}")

@app.get("/")
def read_root():
    """🚨 SECURITY RISK: Exposes secrets in response"""
    return {
        "message": "🚨 Vulnerable Inventory API", 
        "warning": "Contains hardcoded secrets for demonstration",
        "exposed_secrets": {
            "database_url": DATABASE_URL,
            "api_key": THIRD_PARTY_API_KEY,
            "jwt_secret": JWT_SECRET
        }
    }

@app.get("/inventory")
def get_inventory():
    """Get inventory - demonstrates database credential exposure"""
    try:
        # 🚨 SECURITY RISK: Logging database URL
        logger.info(f"Connecting to database: {DATABASE_URL}")
        
        # Simulate database query (no real database needed)
        inventory = get_demo_inventory()
        
        logger.info(f"Retrieved {len(inventory)} items using key: {THIRD_PARTY_API_KEY}")
        
        return {
            "inventory": [{"id": i[0], "name": i[1], "stock": i[2], "price": float(i[3])} for i in inventory],
            "retrieved_with_database": DATABASE_URL,  # 🚨 SECURITY RISK!
            "api_key_used": THIRD_PARTY_API_KEY       # 🚨 SECURITY RISK!
        }
    except Exception as e:
        logger.error(f"Error with database {DATABASE_URL}: {str(e)}")
        raise HTTPException(status_code=500, detail={
            "error": "Database connection failed",
            "database_url": DATABASE_URL
        })

@app.get("/health")
def health_check():
    """🚨 MASSIVE SECURITY RISK: Exposes ALL secrets"""
    return {
        "status": "healthy",
        "secrets_dump": {
            "database_url": DATABASE_URL,
            "api_key": THIRD_PARTY_API_KEY,
            "jwt_secret": JWT_SECRET,
            "stripe_key": STRIPE_SECRET_KEY,
            "aws_access_key": AWS_ACCESS_KEY
        },
        "environment_vars": dict(os.environ)
    }

if __name__ == "__main__":
    import uvicorn
    print(f"🚨 Starting with all secrets: {DATABASE_URL}, {THIRD_PARTY_API_KEY}")
    uvicorn.run(app, host="0.0.0.0", port=8000)