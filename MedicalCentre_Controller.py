
# Controller Class for the Medical Centre Management System

# Importing model classes
from MedicalCentre_ModelClasses import Doctor, Patient, Consultation

class Clinic:
    def __init__(self):
        self.myDoctors = []  # List of Doctor objects
        self.myPatients = []  # List of Patient objects
        self.myConsultations = []  # List of Consultation objects
    
    def add_doctor(self, doctor):
        self.myDoctors.append(doctor)
        
    def add_patient(self, patient):
        self.myPatients.append(patient)
        
    def add_consultation(self, consultation):
        self.myConsultations.append(consultation)
        consultation.myCDoctor.add_consultation(consultation)  # Add the consultation to the doctor's list
        consultation.myCPatient.add_consultation(consultation)  # Add the consultation to the patient's list
        
    def search_doctor_by_id(self, doctor_id):
        for doctor in self.myDoctors:
            if doctor.myDoctorID == doctor_id:
                return doctor
        return None
    
    def search_patient_by_id(self, patient_id):
        for patient in self.myPatients:
            if patient.myPatientID == patient_id:
                return patient
        return None

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
