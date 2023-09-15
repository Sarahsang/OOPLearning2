
# User Interface for the Medical Centre Management System

# Importing controller class
from MedicalCentre_Controller import Clinic, read_doctors_from_file, read_patients_from_file
from MedicalCentre_ModelClasses import Doctor, Patient, Consultation
import re

class InvalidIDError(Exception):
    pass

class NotFoundError(Exception):
    pass

def assign_doctor_to_patient(clinic):
    print("Assign a Doctor to a Patient")
    try:
        patient_id = int(input("Enter Patient ID: "))
        doctor_id = int(input("Enter Doctor ID: "))
    except ValueError:
        print("Invalid ID. IDs should be integers.")
        return

    try:
        patient = clinic.search_patient_by_id(patient_id)
        doctor = clinic.search_doctor_by_id(doctor_id)
        
        if patient is None or doctor is None:
            raise NotFoundError("Invalid Doctor or Patient ID.")
        
        patient.assign_doctor(doctor)
        print(f"Doctor {doctor.get_first_name()} {doctor.get_last_name()} has been assigned to patient {patient.get_first_name()} {patient.get_last_name()}.")
    except NotFoundError as e:
        print(e)



def add_consultation(clinic):
    print("Add a Consultation")
    
    try:
        patient_id = int(input("Enter Patient ID: "))
        doctor_id = int(input("Enter Doctor ID: "))
    except ValueError:
        print("Invalid ID. IDs should be integers.")
        return
    
    try:
        date = input("Enter date (dd/mm/yyyy): ")
        if not re.match(r'\d{2}/\d{2}/\d{4}', date):
            raise ValueError("Invalid date format.")
        
        time = input("Enter time (hh:mm AM/PM): ")
        if not re.match(r'(?:[01]\d|2[0-3]):[0-5]\d [APap][Mm]', time):
            raise ValueError("Invalid time format.")
        
        reason = input("Enter reason: ")
        fee = float(input("Enter fee: "))
        
        patient = clinic.search_patient_by_id(patient_id)
        doctor = clinic.search_doctor_by_id(doctor_id)
        
        if patient is None or doctor is None:
            raise NotFoundError("Invalid Doctor or Patient ID.")
        
        consultation = Consultation(date, time, doctor, patient, reason, fee)
        clinic.add_consultation(consultation)
        print("Consultation added.")
    except (ValueError, NotFoundError) as e:
        print(e)



def get_valid_int_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def view_doctors_info(clinic):
    print("View Doctor's Information")
    doctor_id = get_valid_int_input("Enter Doctor ID: ")
    
    if doctor_id is not None:
        doctor = clinic.search_doctor_by_id(doctor_id)
        if doctor:
            print(doctor)
            print("Patients:")
            for patient in clinic._myPatients:
                if patient.get_doctor() == doctor:
                    print(patient)
            print("Consultations:")
            for consultation in doctor.get_consultations():
                print(consultation)
        else:
            print("Invalid Doctor ID.")

def view_patients_info(clinic):
    print("View Patient's Information")
    patient_id = get_valid_int_input("Enter Patient ID: ")
    
    if patient_id is not None:
        patient = clinic.search_patient_by_id(patient_id)
        if patient:
            print(patient)
            if patient.get_doctor():  
                print(f"Doctor: {patient.get_doctor().get_first_name()} {patient.get_doctor().get_last_name()}")  
            else:
                print("No assigned doctor.")
            print("Consultations:")
            for consultation in patient.get_consultations():  
                print(consultation)
        else:
            print("Invalid Patient ID.")

def view_consultation_report(clinic):
    print("View Consultation Report")
    total_fees = 0
    for consultation in clinic._myConsultations:  
        print(consultation)
        total_fees += consultation.get_fee()  
    print(f"Total Fees: ${total_fees}")

def main_menu():
    print("\nWelcome to the Medical Centre Management System")
    print("1. Assign a doctor to a patient")
    print("2. Add a consultation")
    print("3. View doctor's information")
    print("4. View patient's information")
    print("5. View consultation report")
    print("6. Exit")
    choice = input("Please enter your choice: ")
    return choice

def main():
    # Initialize the clinic and read data from files
    clinic = Clinic()
    read_doctors_from_file("resource/Doctor.txt", clinic)
    read_patients_from_file("resource/Patient.txt", clinic)

    while True:
        choice = main_menu()

        if choice == '1':
            assign_doctor_to_patient(clinic)
        elif choice == '2':
            add_consultation(clinic)
        elif choice == '3':
            view_doctors_info(clinic)
        elif choice == '4':
            view_patients_info(clinic)
        elif choice == '5':
            view_consultation_report(clinic)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
