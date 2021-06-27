"""
This is the patient module and supports all the REST actions for the
doctor patient
"""

from flask import make_response, abort
from app_config import db
from models import Hospital, Patient, PatientSchema


def read_all(hospital_name):
    """
    This function responds to a request for /api/hospital/patients
    with the complete list of patients, of one hospital

    :return:        json string of list of patients
    """
    hospital = Hospital.query.filter_by(name=hospital_name)
    patients = Patient.query.filter(Patient.hospital_id == hospital.id).all()

    # Serialize the data for the response
    patient_schema = PatientSchema(many=True)
    data = patient_schema.dump(patients)
    return data
