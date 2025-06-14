import os

class Config:
    """
    ⚠️ SECURITY WARNING: This configuration contains intentional vulnerabilities
    for demonstration purposes. DO NOT USE IN PRODUCTION!
    """
    
    # 🚨 SECURITY RISK: Hardcoded database credentials
    DATABASE_URL = "postgresql://webapp_user:supersecret123@postgres:5432/webapp_db"
    
    # 🚨 SECURITY RISK: Hardcoded API key
    EXTERNAL_API_KEY = "sk-1234567890abcdef-demo-fake-key"
    
    # 🚨 SECURITY RISK: Hardcoded secret key
    SECRET_KEY = "hardcoded-secret-key-very-bad-practice"
    
    # Additional vulnerable configurations
    JWT_SECRET = "jwt-signing-key-exposed-in-code"
    STRIPE_SECRET_KEY = "sk_test_fake_stripe_key_demo_only"
    SENDGRID_API_KEY = "SG.fake_sendgrid_key_demo_only"
    AWS_ACCESS_KEY = "AKIA_FAKE_AWS_KEY_DEMO"
    AWS_SECRET_KEY = "fake_aws_secret_key_demo_only_not_real"
    
    DEBUG = True