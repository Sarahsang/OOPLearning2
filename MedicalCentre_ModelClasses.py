
# Model Classes for the Medical Centre Management System

class Doctor:
    nextID = 1  # Class variable for generating unique IDs
    
    def __init__(self, first_name, last_name, specialization):
        self._myDoctorFName = first_name  
        self._myDoctorLName = last_name  
        self._myDoctorSpec = specialization  
        self._myDoctorID = Doctor.nextID  
        self._myDoctorCons = []  
        Doctor.nextID += 1  # Increment the ID for the next doctor
    
    # Getter methods
    def get_first_name(self):
        return self._myDoctorFName
    
    def get_last_name(self):
        return self._myDoctorLName
    
    def get_specialization(self):
        return self._myDoctorSpec
    
    def get_id(self):
        return self._myDoctorID
    
    def get_consultations(self):
        return self._myDoctorCons
    
    def get_patient_list(self):
        return [consultation.get_patient() for consultation in self._myDoctorCons]
    
    def get_consultation_list(self):
        return self._myDoctorCons

    # Setter methods
    def set_first_name(self, first_name):
        self._myDoctorFName = first_name
    
    def set_last_name(self, last_name):
        self._myDoctorLName = last_name
    
    def set_specialization(self, specialization):
        self._myDoctorSpec = specialization
    
    def add_consultation(self, consultation):
        self._myDoctorCons.append(consultation)
        
    def __str__(self):
        return f"{self._myDoctorID} {self._myDoctorFName} {self._myDoctorLName} {self._myDoctorSpec}"

class Patient:
    nextID = 1000  # Class variable for generating unique IDs
    
    def __init__(self, first_name, last_name):
        self._myPatientFName = first_name  
        self._myPatientLName = last_name  
        self._myPatientID = Patient.nextID  
        self._myDoctor = None  
        self._myConsultations = []  
        Patient.nextID += 1  # Increment the ID for the next patient
    
    # Getter methods
    def get_first_name(self):
        return self._myPatientFName
    
    def get_last_name(self):
        return self._myPatientLName
    
    def get_id(self):
        return self._myPatientID
    
    def get_doctor(self):
        return self._myDoctor
    
    def get_consultation_list(self):
        return self._myConsultations
    
    # Setter methods
    def set_first_name(self, first_name):
        self._myPatientFName = first_name
    
    def set_last_name(self, last_name):
        self._myPatientLName = last_name
    
    def assign_doctor(self, doctor):
        self._myDoctor = doctor
    
    def add_consultation(self, consultation):
        self._myConsultations.append(consultation)
        
    def __str__(self):
        return f"{self._myPatientID} {self._myPatientFName} {self._myPatientLName}"


class Consultation:
    def __init__(self, date, time, doctor, patient, reason, fee):
        self._myCDate = date  
        self._myCTime = time  
        self._myCDoctor = doctor  
        self._myCPatient = patient  
        self._myCReason = reason  
        self._myFee = fee  
    
    # Getter methods
    def get_date(self):
        return self._myCDate
    
    def get_time(self):  # New getter for time
        return self._myCTime
    
    def get_doctor(self):
        return self._myCDoctor
    
    def get_patient(self):
        return self._myCPatient
    
    def get_reason(self):
        return self._myCReason
    
    def get_fee(self):
        return self._myFee
    
    # Setter methods
    def set_date(self, date):
        self._myCDate = date
    
    def set_time(self, time):  # New setter for time
        self._myCTime = time
    
    def set_doctor(self, doctor):
        self._myCDoctor = doctor
    
    def set_patient(self, patient):
        self._myCPatient = patient
    
    def set_reason(self, reason):
        self._myCReason = reason
    
    def set_fee(self, fee):
        self._myFee = fee
        
    def __str__(self):
        return f"{self._myCDate} {self._myCTime} {self._myCReason} {self._myCPatient.get_first_name()} {self._myCPatient.get_last_name()} ${self._myFee}"
