from prescription_data import patients

trail_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trail_patients:
    patient = trail_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)