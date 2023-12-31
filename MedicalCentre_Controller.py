
# Controller Class for the Medical Centre Management System

# Importing model classes
from MedicalCentre_ModelClasses import Doctor, Patient, Consultation

class Clinic:
    def __init__(self):
        self._myDoctors = []  # List of Doctor objects
        self._myPatients = []  # List of Patient objects
        self._myConsultations = []  # List of Consultation objects
    
    def add_doctor(self, doctor):
        self._myDoctors.append(doctor)
        
    def add_patient(self, patient):
        self._myPatients.append(patient)
        
    def add_consultation(self, consultation):
        self._myConsultations.append(consultation)
        consultation.get_doctor().add_consultation(consultation)   # Add the consultation to the doctor's list
        consultation.get_patient().add_consultation(consultation)  # Add the consultation to the patient's list
        
    def search_doctor_by_id(self, doctor_id):
        for doctor in self._myDoctors:
            if doctor.get_id() == doctor_id:  
                return doctor
        return None
    
    def search_patient_by_id(self, patient_id):
        for patient in self._myPatients:  
            if patient.get_id() == patient_id:  
                return patient
        return None
    
    def get_patient_list_by_doctor(self, doctor_id):
        doctor = self.search_doctor_by_id(doctor_id)
        if doctor:
            return doctor.get_patient_list()
        return []

    def get_consultation_list_by_doctor(self, doctor_id):
        doctor = self.search_doctor_by_id(doctor_id)
        if doctor:
            return doctor.get_consultation_list()
        return []

    def get_consultation_list_by_patient(self, patient_id):
        patient = self.search_patient_by_id(patient_id)
        if patient:
            return patient.get_consultation_list()
        return []

    def get_consults_by_doctor(self, doctor_id):
        doctor = self.search_doctor_by_id(doctor_id)
        if doctor:
            return doctor.get_consultations()
        return []

    def get_consults_by_patient(self, patient_id):
        patient = self.search_patient_by_id(patient_id)
        if patient:
            return [consult for consult in self._myConsultations if consult.get_patient() == patient]
        return []

# File Reading Functions

def read_doctors_from_file(filename, clinic):
    try:
        with open(filename, 'r') as file:
            for line in file:
                first_name, last_name, specialization = line.strip().split(',')
                doctor = Doctor(first_name, last_name, specialization)
                clinic.add_doctor(doctor)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_patients_from_file(filename, clinic):
    try:
        with open(filename, 'r') as file:
            for line in file:
                first_name, last_name = line.strip().split(',')
                patient = Patient(first_name, last_name)
                clinic.add_patient(patient)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
