"""
This is the hospital module and supports all the REST actions for the
hospital data
"""


from flask import make_response, abort
from app_config import db
from models import Hospital, HospitalSchema


def read_all():
    """
    This function responds to a request for /api/hospitals
    with the complete list of hospitals

    :return:        json string of list of hospitals
    """

    hospitals = Hospital.query.order_by(Hospital.id).all()

    # Serialize the data for the response
    hospital_schema = HospitalSchema(many=True)
    data = hospital_schema.dump(hospitals)
    return data
