
# User Interface for the Medical Centre Management System

# Model Classes for the Medical Centre Management System
from MedicalCentre_ModelClasses import Doctor, Patient, Consultation
# Controller Class for the Medical Centre Management System
from MedicalCentre_Controller import Clinic, read_doctors_from_file, read_patients_from_file
from tkinter import Tk, Label, Button, Entry, Listbox, Scrollbar, Frame, Toplevel

import re

class MedicalCentreApp:
    def __init__(self, master):
        self.master = master
        master.title("Medical Centre Management System")
        
        # Initialize the clinic and read data from files
        self.clinic = Clinic()
        read_doctors_from_file("resource/Doctor.txt", self.clinic)
        read_patients_from_file("resource/Patient.txt", self.clinic)

        # Frames
        self.left_frame = Frame(master)
        self.left_frame.grid(row=0, column=0, rowspan=3)

        self.right_frame = Frame(master)
        self.right_frame.grid(row=0, column=1, rowspan=2)

        self.bottom_frame = Frame(master)
        self.bottom_frame.grid(row=2, column=1)

        # Left side: Lists for doctors and patients
        self.doctor_listbox = Listbox(self.left_frame)
        self.doctor_listbox.pack()
        self.patient_listbox = Listbox(self.left_frame)
        self.patient_listbox.pack()

        # Right side: Consultation details
        self.date_label = Label(self.right_frame, text="Date (dd/mm/yyyy):")
        self.date_label.grid(row=0, column=0)
        self.date_entry = Entry(self.right_frame)
        self.date_entry.grid(row=0, column=1)

        self.time_label = Label(self.right_frame, text="Time (hh:mm AM/PM):")
        self.time_label.grid(row=1, column=0)
        self.time_entry = Entry(self.right_frame)
        self.time_entry.grid(row=1, column=1)

        self.reason_label = Label(self.right_frame, text="Reason:")
        self.reason_label.grid(row=2, column=0)
        self.reason_entry = Entry(self.right_frame)
        self.reason_entry.grid(row=2, column=1)

        self.fee_label = Label(self.right_frame, text="Fee:")
        self.fee_label.grid(row=3, column=0)
        self.fee_entry = Entry(self.right_frame)
        self.fee_entry.grid(row=3, column=1)

        # Middle: Assignment and adding consultation
        self.assign_button = Button(self.right_frame, text="Assign Doctor", command=self.assign_doctor_to_patient)
        self.assign_button.grid(row=4, column=0)

        self.add_consultation_button = Button(self.right_frame, text="Add Consultation", command=self.add_consultation)
        self.add_consultation_button.grid(row=4, column=1)

        # Bottom: Information and report buttons
        self.left_frame = Frame(master)
        self.left_frame.grid(row=0, column=0, rowspan=3)

        self.right_frame = Frame(master)
        self.right_frame.grid(row=0, column=1, rowspan=2)

        self.bottom_frame_1 = Frame(master)
        self.bottom_frame_1.grid(row=2, column=0, columnspan=2, sticky='ew')
        self.bottom_frame_1.columnconfigure(0, weight=1)
        self.bottom_frame_1.columnconfigure(1, weight=1)
        self.bottom_frame_1.columnconfigure(2, weight=1)
        self.bottom_frame_1.columnconfigure(3, weight=1)

        self.bottom_frame_2 = Frame(master)
        self.bottom_frame_2.grid(row=3, column=0, columnspan=2, sticky='ew')
        self.bottom_frame_2.columnconfigure(0, weight=1)
        self.bottom_frame_2.columnconfigure(1, weight=1)
        self.bottom_frame_2.columnconfigure(2, weight=1)

        # Bottom: Information and report buttons
        self.top_bottom_frame = Frame(self.bottom_frame)  # First row in the bottom frame
        self.top_bottom_frame.pack(side='top', fill='x', padx=5, pady=5)
        self.bottom_bottom_frame = Frame(self.bottom_frame)  # Second row in the bottom frame
        self.bottom_bottom_frame.pack(side='top', fill='x', padx=5, pady=5)

        self.view_doctors_button = Button(self.top_bottom_frame, text="Doctor Info", command=self.view_doctors_info)
        self.view_doctors_button.pack(side="right", padx=5)

        self.view_patients_button = Button(self.top_bottom_frame, text="Patient Info", command=self.view_patients_info)
        self.view_patients_button.pack(side="right", padx=5)

        self.view_report_button = Button(self.top_bottom_frame, text="Consultation Report", command=self.view_consultation_report)
        self.view_report_button.pack(side="right", padx=5)

        self.close_button = Button(self.top_bottom_frame, text="Exit", command=master.quit)
        self.close_button.pack(side="right", padx=5)

        self.view_patients_by_doctor_button = Button(self.bottom_bottom_frame, text="Patients by Doctor", command=self.view_patients_by_doctor)
        self.view_patients_by_doctor_button.pack(side="right", padx=5)

        self.view_consults_by_doctor_button = Button(self.bottom_bottom_frame, text="Consultations by Doctor", command=self.view_consults_by_doctor)
        self.view_consults_by_doctor_button.pack(side="right", padx=5)

        self.view_consults_by_patient_button = Button(self.bottom_bottom_frame, text="Consultations by Patient", command=self.view_consults_by_patient)
        self.view_consults_by_patient_button.pack(side="right", padx=5)


        # Fill the listboxes
        self.fill_listboxes()

    def fill_listboxes(self):
        for doctor in self.clinic._myDoctors:
            self.doctor_listbox.insert("end", str(doctor))
        for patient in self.clinic._myPatients:
            self.patient_listbox.insert("end", str(patient))

    
    def assign_doctor_to_patient(self):
        self.new_window = Toplevel(self.master)
        self.new_window.title("Assign a Doctor to a Patient")

        Label(self.new_window, text="Enter Patient ID:").grid(row=0, column=0)
        self.patient_id_entry = Entry(self.new_window)
        self.patient_id_entry.grid(row=0, column=1)

        Label(self.new_window, text="Enter Doctor ID:").grid(row=1, column=0)
        self.doctor_id_entry = Entry(self.new_window)
        self.doctor_id_entry.grid(row=1, column=1)

        Button(self.new_window, text="Assign", command=self.perform_assign).grid(row=2, columnspan=2)

    def perform_assign(self):
        try:
            patient_id = int(self.patient_id_entry.get())
            doctor_id = int(self.doctor_id_entry.get())
            patient = self.clinic.search_patient_by_id(patient_id)
            doctor = self.clinic.search_doctor_by_id(doctor_id)
            if patient and doctor:
                patient.assign_doctor(doctor)
                Label(self.new_window, text=f"Assigned {doctor.get_first_name()} to {patient.get_first_name()}").grid(row=3, columnspan=2)
            else:
                Label(self.new_window, text="Invalid IDs").grid(row=3, columnspan=2)
        except ValueError:
            Label(self.new_window, text="Please enter valid IDs").grid(row=3, columnspan=2)

    
    def add_consultation(self):
        self.consult_window = Toplevel(self.master)
        self.consult_window.title("Add a Consultation")

        Label(self.consult_window, text="Enter Patient ID:").grid(row=0, column=0)
        self.consult_patient_id_entry = Entry(self.consult_window)
        self.consult_patient_id_entry.grid(row=0, column=1)

        Label(self.consult_window, text="Enter Doctor ID:").grid(row=1, column=0)
        self.consult_doctor_id_entry = Entry(self.consult_window)
        self.consult_doctor_id_entry.grid(row=1, column=1)

        Label(self.consult_window, text="Enter Date (dd/mm/yyyy):").grid(row=2, column=0)
        self.consult_date_entry = Entry(self.consult_window)
        self.consult_date_entry.grid(row=2, column=1)

        Label(self.consult_window, text="Enter Time (hh:mm AM/PM):").grid(row=3, column=0)
        self.consult_time_entry = Entry(self.consult_window)
        self.consult_time_entry.grid(row=3, column=1)

        Label(self.consult_window, text="Enter Reason:").grid(row=4, column=0)
        self.consult_reason_entry = Entry(self.consult_window)
        self.consult_reason_entry.grid(row=4, column=1)

        Label(self.consult_window, text="Enter Fee:").grid(row=5, column=0)
        self.consult_fee_entry = Entry(self.consult_window)
        self.consult_fee_entry.grid(row=5, column=1)

        Button(self.consult_window, text="Add", command=self.perform_add_consultation).grid(row=6, columnspan=2)

    def perform_add_consultation(self):
        try:
            patient_id = int(self.consult_patient_id_entry.get())
            doctor_id = int(self.consult_doctor_id_entry.get())
            date = self.consult_date_entry.get()
            time = self.consult_time_entry.get()
            reason = self.consult_reason_entry.get()
            fee = float(self.consult_fee_entry.get())

            if not re.match(r'\d{2}/\d{2}/\d{4}', date):
                raise ValueError("Invalid date format.")
            if not re.match(r'(?:[01]\d|2[0-3]):[0-5]\d [AaPp][Mm]', time):
                raise ValueError("Invalid time format.")


            patient = self.clinic.search_patient_by_id(patient_id)
            doctor = self.clinic.search_doctor_by_id(doctor_id)
            if patient and doctor:
                consultation = Consultation(date, time, doctor, patient, reason, fee)
                self.clinic.add_consultation(consultation)
                Label(self.consult_window, text="Consultation added successfully.").grid(row=7, columnspan=2)
            else:
                Label(self.consult_window, text="Invalid Patient or Doctor ID.").grid(row=7, columnspan=2)
        except ValueError as e:
            Label(self.consult_window, text=str(e)).grid(row=7, columnspan=2)

    def view_doctors_info(self):
        self.doc_info_window = Toplevel(self.master)
        self.doc_info_window.title("Doctor's Information")

        Label(self.doc_info_window, text="Enter Doctor ID:").grid(row=0, column=0)
        self.doc_id_entry = Entry(self.doc_info_window)
        self.doc_id_entry.grid(row=0, column=1)
        Button(self.doc_info_window, text="Search", command=self.show_doctor_info).grid(row=1, columnspan=2)

    def show_doctor_info(self):
        try:
            doctor_id = int(self.doc_id_entry.get())
            doctor = self.clinic.search_doctor_by_id(doctor_id)
            if doctor:
                Label(self.doc_info_window, text=str(doctor)).grid(row=2, columnspan=2)
            else:
                Label(self.doc_info_window, text="Doctor not found with the given ID.").grid(row=2, columnspan=2)
        except ValueError:
            Label(self.doc_info_window, text="Please enter a valid doctor ID.").grid(row=2, columnspan=2)

    def view_patients_info(self):
        self.pat_info_window = Toplevel(self.master)
        self.pat_info_window.title("Patient's Information")

        Label(self.pat_info_window, text="Enter Patient ID:").grid(row=0, column=0)
        self.pat_id_entry = Entry(self.pat_info_window)
        self.pat_id_entry.grid(row=0, column=1)
        Button(self.pat_info_window, text="Search", command=self.show_patient_info).grid(row=1, columnspan=2)

    def show_patient_info(self):
        try:
            patient_id = int(self.pat_id_entry.get())
            patient = self.clinic.search_patient_by_id(patient_id)
            if patient:
                Label(self.pat_info_window, text=str(patient)).grid(row=2, columnspan=2)
                if patient.get_doctor():
                    Label(self.pat_info_window, text=f"Doctor: {patient.get_doctor().get_first_name()} {patient.get_doctor().get_last_name()}").grid(row=3, columnspan=2)
            else:
                Label(self.pat_info_window, text="Patient not found with the given ID.").grid(row=2, columnspan=2)
        except ValueError:
            Label(self.pat_info_window, text="Please enter a valid patient ID.").grid(row=2, columnspan=2)

    def view_consultation_report(self):
        self.report_window = Toplevel(self.master)
        self.report_window.title("Consultation Report")

        listbox = Listbox(self.report_window, width=70)
        scrollbar = Scrollbar(self.report_window)
        scrollbar.pack(side="right", fill="y")
        listbox.pack(side="left", fill="both")
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        total_fees = 0
        for consultation in self.clinic._myConsultations:
            listbox.insert("end", str(consultation))
            total_fees += consultation.get_fee()

        Label(self.report_window, text=f"Total Fees: ${total_fees}").pack()
        
    # For viewing patients by a specific doctor
    def view_patients_by_doctor(self):
        self.pat_by_doc_window = Toplevel(self.master)
        self.pat_by_doc_window.title("Patients by Doctor")
        
        Label(self.pat_by_doc_window, text="Enter Doctor ID:").grid(row=0, column=0)
        self.doc_id_for_pat_list_entry = Entry(self.pat_by_doc_window)
        self.doc_id_for_pat_list_entry.grid(row=0, column=1)
        Button(self.pat_by_doc_window, text="Search", command=self.show_patient_list_by_doctor).grid(row=1, columnspan=2)

    def show_patient_list_by_doctor(self):
        try:
            doctor_id = int(self.doc_id_for_pat_list_entry.get())
            patients = self.clinic.get_patient_list_by_doctor(doctor_id)
            row = 2
            for patient in patients:
                Label(self.pat_by_doc_window, text=str(patient)).grid(row=row, columnspan=2)
                row += 1
        except ValueError:
            Label(self.pat_by_doc_window, text="Please enter a valid doctor ID.").grid(row=row, columnspan=2)

    def view_consults_by_doctor(self):
        self.consults_by_doc_window = Toplevel(self.master)
        self.consults_by_doc_window.title("Consultations by Doctor")
        
        Label(self.consults_by_doc_window, text="Enter Doctor ID:").grid(row=0, column=0)
        self.doc_id_for_consults_entry = Entry(self.consults_by_doc_window)
        self.doc_id_for_consults_entry.grid(row=0, column=1)
        Button(self.consults_by_doc_window, text="Search", command=self.show_consults_by_doctor).grid(row=1, columnspan=2)

    def show_consults_by_doctor(self):
        try:
            doctor_id = int(self.doc_id_for_consults_entry.get())
            consultations = self.clinic.get_consults_by_doctor(doctor_id)
            row = 2
            for consult in consultations:
                Label(self.consults_by_doc_window, text=str(consult)).grid(row=row, columnspan=2)
                row += 1
        except ValueError:
            Label(self.consults_by_doc_window, text="Please enter a valid doctor ID.").grid(row=row, columnspan=2)

    def view_consults_by_patient(self):
        self.consults_by_pat_window = Toplevel(self.master)
        self.consults_by_pat_window.title("Consultations by Patient")
        
        Label(self.consults_by_pat_window, text="Enter Patient ID:").grid(row=0, column=0)
        self.pat_id_for_consults_entry = Entry(self.consults_by_pat_window)
        self.pat_id_for_consults_entry.grid(row=0, column=1)
        Button(self.consults_by_pat_window, text="Search", command=self.show_consults_by_patient).grid(row=1, columnspan=2)

    def show_consults_by_patient(self):
        try:
            patient_id = int(self.pat_id_for_consults_entry.get())
            consultations = self.clinic.get_consults_by_patient(patient_id)
            row = 2
            for consult in consultations:
                Label(self.consults_by_pat_window, text=str(consult)).grid(row=row, columnspan=2)
                row += 1
        except ValueError:
            Label(self.consults_by_pat_window, text="Please enter a valid patient ID.").grid(row=row, columnspan=2)

if __name__ == "__main__":
    root = Tk()
    app = MedicalCentreApp(root)
    root.mainloop()