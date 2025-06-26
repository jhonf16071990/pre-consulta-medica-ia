# Medical Pre-consultation Backend

Backend service for the medical pre-consultation application with AI-powered triage system.

## Features

- Modular Flask application structure
- RESTful API endpoints for triage and user management
- Voice processing capabilities (text-to-speech and speech-to-text)
- Data models for triage, patients, and users
- CORS support for frontend integration

## Requirements

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory:
```bash
touch .env
```

4. Add the following environment variables to .env:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python run.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### Triage

- POST `/api/v1/triage/symptoms` - Submit symptoms for triage
- POST `/api/v1/triage/voice/input` - Process voice input
- POST `/api/v1/triage/voice/output` - Convert text to speech

### User Management

- GET `/api/v1/users/profile` - Get user profile
- GET `/api/v1/users/consultation-history` - Get consultation history
- PUT `/api/v1/users/update-profile` - Update user profile
- GET/PUT `/api/v1/users/preferences` - Get/update user preferences

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── triage.py
│   │   └── user.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── triage.py
│   │   └── user.py
│   └── utils/
│       ├── __init__.py
│       └── voice.py
├── config.py
├── requirements.txt
└── run.py
```

## Development

- Models are defined in `app/models/`
- Routes are defined in `app/routes/`
- Utility functions are in `app/utils/`
- Configuration settings are in `config.py`

## Testing

To run tests (once implemented):
```bash
python -m pytest
```

## Next Steps

1. Implement database integration
2. Add authentication and authorization
3. Implement actual triage classification logic
4. Add comprehensive testing
5. Set up CI/CD pipeline
