import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    FLASK_APP = 'run.py'
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    
    # API configurations
    API_TITLE = 'Medical Pre-consultation API'
    API_VERSION = 'v1'
    
    # CORS settings
    CORS_HEADERS = 'Content-Type'
    
    # Voice settings
    VOICE_LANGUAGE = 'es'  # Spanish voice
    VOICE_RATE = 150  # Speech rate
    
    # Triage settings
    MAX_SYMPTOMS = 10  # Maximum number of symptoms per consultation
    MIN_SEVERITY = 1   # Minimum severity level
    MAX_SEVERITY = 5   # Maximum severity level
