from flask import Flask
from flask_cors import CORS
from config import Config

def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize CORS
    CORS(app)
    
    # Register blueprints
    from app.routes import triage_bp, user_bp
    app.register_blueprint(triage_bp, url_prefix='/api/v1/triage')
    app.register_blueprint(user_bp, url_prefix='/api/v1/users')
    
    # Health check route
    @app.route('/health')
    def health_check():
        return {'status': 'healthy', 'version': app.config['API_VERSION']}
    
    return app
