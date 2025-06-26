from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime

@dataclass
class MedicalHistory:
    conditions: List[str]
    allergies: List[str]
    medications: List[str]
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'conditions': self.conditions,
            'allergies': self.allergies,
            'medications': self.medications
        }

@dataclass
class ConsultationRecord:
    date: datetime
    symptoms: List[str]
    triage_level: int
    recommendation: str
    notes: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'date': self.date.isoformat(),
            'symptoms': self.symptoms,
            'triage_level': self.triage_level,
            'recommendation': self.recommendation,
            'notes': self.notes
        }

@dataclass
class UserPreferences:
    language: str = 'es'
    notifications_enabled: bool = True
    voice_enabled: bool = True
    avatar_enabled: bool = True
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'language': self.language,
            'notifications_enabled': self.notifications_enabled,
            'voice_enabled': self.voice_enabled,
            'avatar_enabled': self.avatar_enabled
        }

@dataclass
class User:
    id: str
    name: str
    age: int
    gender: str  # 'M' or 'F'
    email: str
    medical_history: MedicalHistory
    consultation_history: List[ConsultationRecord]
    preferences: UserPreferences
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def validate(self) -> tuple[bool, str]:
        """Validate user data."""
        if not self.name:
            return False, "Name is required"
            
        if not isinstance(self.age, int) or self.age < 0:
            return False, "Invalid age"
            
        if self.gender not in ['M', 'F']:
            return False, "Gender must be 'M' or 'F'"
            
        if not self.email or '@' not in self.email:
            return False, "Valid email is required"
            
        return True, ""

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'email': self.email,
            'medical_history': self.medical_history.to_dict(),
            'consultation_history': [
                consultation.to_dict() 
                for consultation in self.consultation_history
            ],
            'preferences': self.preferences.to_dict(),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def add_consultation(self, consultation: ConsultationRecord) -> None:
        """Add a consultation record to history."""
        self.consultation_history.append(consultation)
        self.updated_at = datetime.now()

    def update_preferences(self, preferences: Dict) -> None:
        """Update user preferences."""
        self.preferences = UserPreferences(**preferences)
        self.updated_at = datetime.now()

    def update_medical_history(self, medical_history: Dict) -> None:
        """Update medical history."""
        self.medical_history = MedicalHistory(**medical_history)
        self.updated_at = datetime.now()
