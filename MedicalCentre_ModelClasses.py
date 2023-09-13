
# Model Classes for the Medical Centre Management System

class Doctor:
    nextID = 1  # Class variable for generating unique IDs
    
    def __init__(self, first_name, last_name, specialization):
        self.myDoctorFName = first_name
        self.myDoctorLName = last_name
        self.myDoctorSpec = specialization
        self.myDoctorID = Doctor.nextID
        self.myDoctorCons = []  # List of Consultations
        Doctor.nextID += 1  # Increment the ID for the next doctor
        
    def add_consultation(self, consultation):
        self.myDoctorCons.append(consultation)
        
    def __str__(self):
        return f"{self.myDoctorID} {self.myDoctorFName} {self.myDoctorLName} {self.myDoctorSpec}"

class Patient:
    nextID = 100  # Class variable for generating unique IDs
    
    def __init__(self, first_name, last_name):
        self.myPatientFName = first_name
        self.myPatientLName = last_name
        self.myPatientID = Patient.nextID
        self.myDoctor = None  # Doctor object
        self.myConsultations = []  # List of Consultations
        Patient.nextID += 1  # Increment the ID for the next patient
        
    def assign_doctor(self, doctor):
        self.myDoctor = doctor
        
    def add_consultation(self, consultation):
        self.myConsultations.append(consultation)
        
    def __str__(self):
        return f"{self.myPatientID} {self.myPatientFName} {self.myPatientLName}"

class Consultation:
    def __init__(self, date, doctor, patient, reason, fee):
        self.myCDate = date
        self.myCDoctor = doctor
        self.myCPatient = patient
        self.myCReason = reason
        self.myFee = fee
        
    def __str__(self):
        return f"{self.myCDate} {self.myCReason} {self.myCPatient.myPatientFName} {self.myCPatient.myPatientLName} ${self.myFee}"
