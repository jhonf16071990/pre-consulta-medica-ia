import pyttsx3
import speech_recognition as sr
from flask import current_app

def text_to_speech(text: str, language: str = None) -> bool:
    """
    Convert text to speech.
    
    Args:
        text (str): Text to convert to speech
        language (str, optional): Language code (e.g., 'es'). Defaults to config value.
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        engine = pyttsx3.init()
        
        # Set language
        if language is None:
            language = current_app.config['VOICE_LANGUAGE']
        
        # Configure voice properties
        engine.setProperty('rate', current_app.config['VOICE_RATE'])
        
        # Get available voices and set Spanish voice if available
        voices = engine.getProperty('voices')
        spanish_voice = next((v for v in voices if language in v.languages), None)
        if spanish_voice:
            engine.setProperty('voice', spanish_voice.id)
        
        # Convert text to speech
        engine.say(text)
        engine.runAndWait()
        
        return True
        
    except Exception as e:
        current_app.logger.error(f"Text to speech conversion failed: {str(e)}")
        return False

def speech_to_text(audio_data) -> tuple[bool, str]:
    """
    Convert speech to text.
    
    Args:
        audio_data: Audio data to convert
    
    Returns:
        tuple[bool, str]: (success, text/error_message)
    """
    try:
        recognizer = sr.Recognizer()
        
        # Convert audio data to text
        with sr.AudioFile(audio_data) as source:
            audio = recognizer.record(source)
            
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(
            audio,
            language=current_app.config['VOICE_LANGUAGE']
        )
        
        return True, text
        
    except sr.UnknownValueError:
        return False, "Could not understand audio"
    except sr.RequestError as e:
        return False, f"Speech recognition service error: {str(e)}"
    except Exception as e:
        current_app.logger.error(f"Speech to text conversion failed: {str(e)}")
        return False, f"Speech to text conversion failed: {str(e)}"
