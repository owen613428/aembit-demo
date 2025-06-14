from flask import Flask, render_template, jsonify, request
import logging
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db_connection():
    """
    🚨 SECURITY RISK: Using hardcoded credentials and logging connection details
    DEMO NOTE: Uses simulated database since no real database setup required
    """
    logger.info(f"Connecting to database with URL: {app.config['DATABASE_URL']}")
    
    # Simulate database connection for demo (no real database needed)
    logger.info("✅ Demo: Simulated database connection established")
    return "simulated_connection"

def get_demo_products():
    """Simulated product data for demo (no real database needed)"""
    return [
        (1, 'MacBook Pro', 2499.99, 'Apple MacBook Pro 16-inch'),
        (2, 'iPhone 15 Pro', 999.99, 'Latest iPhone with Pro features'),
        (3, 'AirPods Pro', 249.99, 'Wireless earbuds with noise cancellation'),
        (4, 'iPad Air', 599.99, 'Versatile tablet for work and play'),
        (5, 'Apple Watch', 399.99, 'Smart watch with health features')
    ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    """Get products - demonstrates database credential exposure"""
    try:
        conn = get_db_connection()  # Simulated connection
        products = get_demo_products()  # Simulated data
        
        # 🚨 SECURITY RISK: Logging API key usage
        logger.info(f"Retrieved {len(products)} products using API key: {app.config['EXTERNAL_API_KEY']}")
        
        return jsonify([{
            'id': p[0], 
            'name': p[1], 
            'price': float(p[2]),
            'description': p[3]
        } for p in products])
    except Exception as e:
        # 🚨 SECURITY RISK: Error logging exposes database credentials
        logger.error(f"Database error with credentials {app.config['DATABASE_URL']}: {str(e)}")
        return jsonify({'error': 'Database connection failed', 'details': str(e)}), 500

@app.route('/api/external-data')
def get_external_data():
    """Simulate external API call - demonstrates API key exposure"""
    headers = {
        'Authorization': f'Bearer {app.config["EXTERNAL_API_KEY"]}',
        'Content-Type': 'application/json'
    }
    
    # 🚨 SECURITY RISK: Logging the API key
    logger.info(f"Making external API call with key: {app.config['EXTERNAL_API_KEY']}")
    
    return jsonify({
        'message': 'External API data retrieved',
        'api_key_used': app.config['EXTERNAL_API_KEY'],  # 🚨 NEVER DO THIS!
        'data': ['customer_data_1', 'customer_data_2', 'customer_data_3'],
        'timestamp': '2025-06-13T10:00:00Z'
    })

@app.route('/api/health')
def health_check():
    """
    🚨 MASSIVE SECURITY RISK: Exposes all secrets!
    This demonstrates how health/debug endpoints can accidentally expose secrets
    """
    return jsonify({
        'status': 'healthy',
        'secrets_exposed': True,
        'database_url': app.config['DATABASE_URL'],  # 🚨 MASSIVE SECURITY RISK!
        'api_key': app.config['EXTERNAL_API_KEY'],    # 🚨 MASSIVE SECURITY RISK!
        'jwt_secret': app.config['JWT_SECRET'],       # 🚨 MASSIVE SECURITY RISK!
        'stripe_key': app.config['STRIPE_SECRET_KEY'], # 🚨 MASSIVE SECURITY RISK!
        'aws_credentials': {
            'access_key': app.config['AWS_ACCESS_KEY'],
            'secret_key': app.config['AWS_SECRET_KEY']
        },
        'environment_vars': dict(os.environ)
    })

if __name__ == '__main__':
    # 🚨 SECURITY RISK: Logging secrets at startup
    logger.info("Starting vulnerable web application")
    logger.info(f"Database: {app.config['DATABASE_URL']}")
    logger.info(f"API Key: {app.config['EXTERNAL_API_KEY']}")
    
    app.run(host='0.0.0.0', port=3000, debug=True)