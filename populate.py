from hospital import Doctor, Patient, Nurse, session


#ADDING DOCTORS

# doctor_1 = Doctor(name = 'Dr. Kazi', specialization='Allergists')
# doctor_2 = Doctor(name = 'Dr. Jaro', specialization = 'Dermatologists')
# doctor_3 = Doctor(name = 'Dr. Mamboleo', specialization = 'Cardiologists')

# session.add_all(
#     [doctor_1, doctor_2, doctor_3]
# )
# session.commit()



#ADDING NURSES

nurse_1 = Nurse(name = 'Mr. Jojo', shift= 'Night')
nurse_2 = Nurse(name = 'Mrs. Didi', shift = 'Day')
nurse_3 = Nurse(name = 'Mrs.Njoro', shift = 'Night')
nurse_4 = Nurse(name = 'Mrs. Ziba', shift = 'Day')

session.add_all(
    [nurse_1, nurse_2, nurse_3, nurse_4]
)

session.commit()