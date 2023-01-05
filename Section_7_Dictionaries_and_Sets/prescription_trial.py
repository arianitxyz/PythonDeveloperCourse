from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    print(patient, prescription)
