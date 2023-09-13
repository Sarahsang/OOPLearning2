
# User Interface for the Medical Centre Management System

# Importing controller class
from MedicalCentre_Controller import Clinic, read_doctors_from_file, read_patients_from_file

def assign_doctor_to_patient(clinic):
    print("Assign a Doctor to a Patient")
    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    
    patient = clinic.search_patient_by_id(patient_id)
    doctor = clinic.search_doctor_by_id(doctor_id)
    
    if patient and doctor:
        patient.assign_doctor(doctor)
        print(f"Doctor {doctor.myDoctorFName} {doctor.myDoctorLName} has been assigned to patient {patient.myPatientFName} {patient.myPatientLName}.")
    else:
        print("Invalid Doctor or Patient ID.")

def add_consultation(clinic):
    print("Add a Consultation")
    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    date = input("Enter date (dd/mm/yyyy): ")
    reason = input("Enter reason: ")
    fee = float(input("Enter fee: "))
    
    patient = clinic.search_patient_by_id(patient_id)
    doctor = clinic.search_doctor_by_id(doctor_id)
    
    if patient and doctor:
        consultation = Consultation(date, doctor, patient, reason, fee)
        clinic.add_consultation(consultation)
        print("Consultation added.")
    else:
        print("Invalid Doctor or Patient ID.")

def view_doctors_info(clinic):
    print("View Doctor's Information")
    doctor_id = int(input("Enter Doctor ID: "))
    doctor = clinic.search_doctor_by_id(doctor_id)
    
    if doctor:
        print(doctor)
        print("Patients:")
        for patient in clinic.myPatients:
            if patient.myDoctor == doctor:
                print(patient)
        print("Consultations:")
        for consultation in doctor.myDoctorCons:
            print(consultation)
    else:
        print("Invalid Doctor ID.")

def view_patients_info(clinic):
    print("View Patient's Information")
    patient_id = int(input("Enter Patient ID: "))
    patient = clinic.search_patient_by_id(patient_id)
    
    if patient:
        print(patient)
        if patient.myDoctor:
            print(f"Doctor: {patient.myDoctor.myDoctorFName} {patient.myDoctor.myDoctorLName}")
        else:
            print("No assigned doctor.")
        print("Consultations:")
        for consultation in patient.myConsultations:
            print(consultation)
    else:
        print("Invalid Patient ID.")

def view_consultation_report(clinic):
    print("View Consultation Report")
    total_fees = 0
    for consultation in clinic.myConsultations:
        print(consultation)
        total_fees += consultation.myFee
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
