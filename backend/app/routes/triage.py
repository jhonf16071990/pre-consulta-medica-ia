from flask import jsonify, request
from app.routes import triage_bp
from app.utils.voice import text_to_speech, speech_to_text

@triage_bp.route('/symptoms', methods=['POST'])
def submit_symptoms():
    """
    Submit symptoms for triage classification.
    Expected payload:
    {
        "symptoms": [
            {
                "description": "dolor de cabeza",
                "severity": 3,
                "duration": "2 días"
            }
        ],
        "patient": {
            "age": 35,
            "gender": "M",
            "preexisting_conditions": []
        }
    }
    """
    data = request.get_json()
    
    # Validate request data
    if not data or 'symptoms' not in data or 'patient' not in data:
        return jsonify({
            'error': 'Invalid request data',
            'required_fields': ['symptoms', 'patient']
        }), 400
    
    # TODO: Implement triage classification logic
    # For now, return a mock response
    triage_result = {
        'urgency_level': 3,  # 1-5 scale
        'recommendation': 'Consulta médica dentro de 24 horas',
        'symptoms_analysis': [
            {
                'symptom': symptom['description'],
                'severity': symptom['severity'],
                'notes': 'Requiere evaluación profesional'
            }
            for symptom in data['symptoms']
        ],
        'next_steps': [
            'Programar cita médica',
            'Monitorear síntomas',
            'Mantener reposo'
        ]
    }
    
    return jsonify(triage_result)

@triage_bp.route('/voice/input', methods=['POST'])
def voice_input():
    """
    Process voice input and convert to text.
    Expects audio data in the request.
    """
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
        
    audio_file = request.files['audio']
    
    try:
        # TODO: Implement actual speech to text conversion
        # For now, return mock response
        text = "Tengo dolor de cabeza y fiebre desde hace dos días"
        
        return jsonify({
            'success': True,
            'text': text
        })
    except Exception as e:
        return jsonify({
            'error': 'Failed to process voice input',
            'details': str(e)
        }), 500

@triage_bp.route('/voice/output', methods=['POST'])
def voice_output():
    """
    Convert text to speech.
    Expected payload: {"text": "Text to convert to speech"}
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
        
    try:
        # TODO: Implement actual text to speech conversion
        # For now, return success without audio
        return jsonify({
            'success': True,
            'message': 'Text converted to speech successfully'
        })
    except Exception as e:
        return jsonify({
            'error': 'Failed to convert text to speech',
            'details': str(e)
        }), 500
