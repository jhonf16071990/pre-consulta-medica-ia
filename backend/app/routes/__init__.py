from flask import Blueprint

# Create blueprints
triage_bp = Blueprint('triage', __name__)
user_bp = Blueprint('user', __name__)

# Import routes
from app.routes import triage, user

# Export blueprints
__all__ = ['triage_bp', 'user_bp']
