from flask import jsonify, request
from app.routes import user_bp

@user_bp.route('/profile', methods=['GET'])
def get_profile():
    """Get user profile information."""
    # TODO: Implement actual user authentication and profile retrieval
    # For now, return mock data
    profile = {
        'id': '12345',
        'name': 'Juan Pérez',
        'age': 35,
        'gender': 'M',
        'medical_history': {
            'conditions': ['Hipertensión'],
            'allergies': ['Penicilina'],
            'medications': ['Enalapril']
        },
        'consultation_history': [
            {
                'date': '2024-03-15',
                'symptoms': ['Dolor de cabeza', 'Fiebre'],
                'triage_level': 3,
                'recommendation': 'Consulta médica dentro de 24 horas'
            }
        ]
    }
    return jsonify(profile)

@user_bp.route('/consultation-history', methods=['GET'])
def get_consultation_history():
    """Get user's consultation history."""
    # TODO: Implement actual consultation history retrieval
    # For now, return mock data
    history = [
        {
            'id': '1',
            'date': '2024-03-15',
            'symptoms': ['Dolor de cabeza', 'Fiebre'],
            'triage_level': 3,
            'recommendation': 'Consulta médica dentro de 24 horas'
        },
        {
            'id': '2',
            'date': '2024-03-10',
            'symptoms': ['Dolor de garganta'],
            'triage_level': 2,
            'recommendation': 'Seguimiento en casa'
        }
    ]
    return jsonify(history)

@user_bp.route('/update-profile', methods=['PUT'])
def update_profile():
    """Update user profile information."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
        
    # TODO: Implement actual profile update
    # For now, return success response
    return jsonify({
        'success': True,
        'message': 'Profile updated successfully'
    })

@user_bp.route('/preferences', methods=['GET', 'PUT'])
def handle_preferences():
    """Get or update user preferences."""
    if request.method == 'GET':
        # TODO: Implement actual preference retrieval
        # For now, return mock data
        preferences = {
            'language': 'es',
            'notifications_enabled': True,
            'voice_enabled': True,
            'avatar_enabled': True
        }
        return jsonify(preferences)
    
    else:  # PUT
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
            
        # TODO: Implement actual preference update
        # For now, return success response
        return jsonify({
            'success': True,
            'message': 'Preferences updated successfully'
        })
