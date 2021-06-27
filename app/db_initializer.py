import os

from app_config import db
from models import Hospital, User, Doctor, Patient, Visit


# Delete database file if it exists currently
if os.path.exists("hospital.db"):
    os.remove("hospital.db")


# Data to initialize database with

# Create the database
db.create_all()

# ----------------ADDING HOSPITALS------------------------------------------

HOSPITAL = [
    {"name": "Kamla Nehru", "category": "Dental", "city": "Pune"},
    {"name": "Reliance Hospital", "category": "Vision", "city": "Mumbai"},
    {"name": "KEMs", "category": "ENT", "city": "Bangalore"},
]

hospital_1 = Hospital(
    name=HOSPITAL[0].get("name"),
    category=HOSPITAL[0].get("category"),
    city=HOSPITAL[0].get("city"),
)

hospital_2 = Hospital(
    name=HOSPITAL[1].get("name"),
    category=HOSPITAL[1].get("category"),
    city=HOSPITAL[1].get("city"),
)

hospital_3 = Hospital(
    name=HOSPITAL[2].get("name"),
    category=HOSPITAL[2].get("category"),
    city=HOSPITAL[2].get("city"),
)

db.session.add(hospital_1)
db.session.add(hospital_2)
db.session.add(hospital_3)


db.session.commit()
print("SUCCESS: Hospitals table created.")

# ----------------ADDING USERS------------------------------------------

USER = [
    {"login_name": "ruthra", "role": "admin",
        "password": "admin@123", "fullname": "Ruthra Ved"},
    {"login_name": "shivam", "role": "patient",
        "password": "doc@123", "fullname": "Shivam Bala"},
    {"login_name": "raju", "role": "doctor",
        "password": "raju@123", "fullname": "Raju Bala"},
    {"login_name": "lizu", "role": "doctor",
     "password": "lizu@123", "fullname": "Liza Bala"},
]

user_0 = User(
    login_name=USER[0].get("login_name"),
    role=USER[0].get("role"),
    password=USER[0].get("password"),
    fullname=USER[0].get("fullname"),
)

user_1 = User(
    login_name=USER[1].get("login_name"),
    role=USER[1].get("role"),
    password=USER[1].get("password"),
    fullname=USER[1].get("fullname"),
)

user_2 = User(
    login_name=USER[2].get("login_name"),
    role=USER[2].get("role"),
    password=USER[2].get("password"),
    fullname=USER[2].get("fullname"),
)

user_3 = User(
    login_name=USER[3].get("login_name"),
    role=USER[3].get("role"),
    password=USER[3].get("password"),
    fullname=USER[3].get("fullname"),
)

db.session.add(user_0)
db.session.add(user_1)
db.session.add(user_2)
db.session.add(user_3)

db.session.commit()
print("SUCCESS: Users table created.")

# ----------------ADDING DOCTORS------------------------------------------

HOSPITAL_ID = (Hospital.query.get(1)).id

DOCTOR = [
    {"designaton": "Senior",
        "speciality": "Dentist", "hospital_id": HOSPITAL_ID},
    {"designaton": "Junior",
     "speciality": "ENT", "hospital_id": HOSPITAL_ID},
]

doctor_senior = Doctor(
    user=User.query.get(3),
    designaton=DOCTOR[0].get("designaton"),
    speciality=DOCTOR[0].get("speciality"),
    hospital_id=DOCTOR[0].get("hospital_id"),
)

doctor_junior = Doctor(
    user=User.query.get(4),
    designaton=DOCTOR[1].get("designaton"),
    speciality=DOCTOR[1].get("speciality"),
    hospital_id=DOCTOR[1].get("hospital_id"),
)

db.session.add(doctor_senior)
db.session.add(doctor_junior)

db.session.commit()
print("SUCCESS: Doctors table created.")


# ----------------ADDING PATIENTS------------------------------------------

PATIENT = [
    {"age": 34,
        "gender": "Male", "hospital_id": HOSPITAL_ID},
]

patient_1 = Patient(
    user=User.query.get(2),
    age=PATIENT[0].get("age"),
    gender=PATIENT[0].get("gender"),
    hospital_id=PATIENT[0].get("hospital_id"),
)

db.session.add(patient_1)

db.session.commit()
print("SUCCESS: Patients table created.")


# ----------------ADDING VISITS------------------------------------------

VISIT = [
    {"doctor_id": (Doctor.query.get(1)).id,
        "patient_id": (Patient.query.get(1)).id, "prescription": "You are sick. Take this mornning and evening",
        "appointment_status": "Pending"
     },
    {"doctor_id": (Doctor.query.get(2)).id,
        "patient_id": (Patient.query.get(1)).id, "prescription": "You are going deaf. Please use less earphones",
        "appointment_status": "Complete"
     },
]

visit_1 = Visit(
    doctor_id=VISIT[0].get("doctor_id"),
    patient_id=VISIT[0].get("patient_id"),
    prescription=VISIT[0].get("prescription"),
    appointment_status=VISIT[0].get("appointment_status"),
)

visit_2 = Visit(
    doctor_id=VISIT[1].get("doctor_id"),
    patient_id=VISIT[1].get("patient_id"),
    prescription=VISIT[1].get("prescription"),
    appointment_status=VISIT[1].get("appointment_status"),
)

db.session.add(visit_1)
db.session.add(visit_2)

db.session.commit()
print("SUCCESS: Visits table created.")


# -----Displaying Tables-----

hospitals = Hospital.query.all()
users = User.query.all()
doctors = Doctor.query.all()
patients = Patient.query.all()
visits = Visit.query.all()

hospital_list = []
for hospital in hospitals:
    hospital_list.append(hospital)

user_list = []
for user in users:
    user_list.append(user)

doctor_list = []
for doctor in doctors:
    doctor_list.append(doctor)

patient_list = []
for patient in patients:
    patient_list.append(patients)

visit_list = []
for visit in visits:
    visit_list.append(visit)

print("--------------------------HOSPITAL LIST--------------------------")
print(hospital_list)
print("--------------------------USER LIST--------------------------")
print(user_list)
print("--------------------------DOCTOR LIST--------------------------")
print(doctor_list)
print("--------------------------PATIENT LIST--------------------------")
print(patient_list)
print("--------------------------VISIT LIST--------------------------")
print(visit_list)
