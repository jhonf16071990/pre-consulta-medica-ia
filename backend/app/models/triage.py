from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Symptom:
    description: str
    severity: int  # 1-5 scale
    duration: str
    location: Optional[str] = None
    notes: Optional[str] = None

    def validate(self) -> tuple[bool, str]:
        """Validate symptom data."""
        if not self.description:
            return False, "Symptom description is required"
        
        if not isinstance(self.severity, int) or not 1 <= self.severity <= 5:
            return False, "Severity must be an integer between 1 and 5"
            
        if not self.duration:
            return False, "Duration is required"
            
        return True, ""

@dataclass
class Patient:
    age: int
    gender: str  # 'M' or 'F'
    preexisting_conditions: List[str]
    allergies: Optional[List[str]] = None
    medications: Optional[List[str]] = None

    def validate(self) -> tuple[bool, str]:
        """Validate patient data."""
        if not isinstance(self.age, int) or self.age < 0:
            return False, "Invalid age"
            
        if self.gender not in ['M', 'F']:
            return False, "Gender must be 'M' or 'F'"
            
        if not isinstance(self.preexisting_conditions, list):
            return False, "Preexisting conditions must be a list"
            
        return True, ""

@dataclass
class TriageConsultation:
    patient: Patient
    symptoms: List[Symptom]
    timestamp: datetime = datetime.now()
    urgency_level: Optional[int] = None  # 1-5 scale
    recommendation: Optional[str] = None
    next_steps: Optional[List[str]] = None

    def validate(self) -> tuple[bool, str]:
        """Validate consultation data."""
        # Validate patient
        valid, msg = self.patient.validate()
        if not valid:
            return False, f"Invalid patient data: {msg}"
            
        # Validate symptoms
        if not self.symptoms:
            return False, "At least one symptom is required"
            
        for symptom in self.symptoms:
            valid, msg = symptom.validate()
            if not valid:
                return False, f"Invalid symptom data: {msg}"
                
        # Validate urgency level if set
        if self.urgency_level is not None:
            if not isinstance(self.urgency_level, int) or not 1 <= self.urgency_level <= 5:
                return False, "Urgency level must be an integer between 1 and 5"
                
        return True, ""

    def classify_urgency(self) -> None:
        """
        Classify the urgency level based on symptoms and patient data.
        Updates the urgency_level, recommendation, and next_steps fields.
        """
        # TODO: Implement actual urgency classification logic
        # For now, use a simple average of symptom severities
        total_severity = sum(s.severity for s in self.symptoms)
        avg_severity = total_severity / len(self.symptoms)
        self.urgency_level = round(avg_severity)
        
        # Set recommendation based on urgency level
        recommendations = {
            1: "Seguimiento en casa",
            2: "Consulta médica en los próximos días",
            3: "Consulta médica dentro de 24 horas",
            4: "Atención urgente en centro médico",
            5: "Llamar ambulancia / Acudir a emergencias"
        }
        self.recommendation = recommendations.get(self.urgency_level, "Consultar con un médico")
        
        # Set next steps
        self.next_steps = [
            "Monitorear síntomas",
            "Mantener reposo",
            self.recommendation
        ]
