"""
This is the doctor module and supports all the REST actions for the
doctor data
"""

from flask import make_response, abort
from app_config import db
from models import Hospital, Doctor, DoctorSchema


def read_all(hospital_name):
    """
    This function responds to a request for /api/hospital/doctors
    with the complete list of doctors, of one hospital

    :return:        json string of list of hospitals
    """
    hospital = Hospital.query.filter_by(name=hospital_name)
    doctors = Doctor.query.filter(Doctor.hospital_id == hospital.id).all()

    # Serialize the data for the response
    doctor_schema = DoctorSchema(many=True)
    data = doctor_schema.dump(doctors)
    return data
