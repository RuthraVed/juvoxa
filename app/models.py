from datetime import datetime

from app_config import db, ma


# -------HOSPITAL MODEL-------------------------

class Hospital(db.Model):
    __tablename__ = "hospital"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    category = db.Column(db.String(32), default="None")
    city = db.Column(db.String(32), nullable=False)
    doctors = db.relationship(
        'Doctor', backref='hospital', lazy=True)
    patients = db.relationship(
        'Patient', backref='hospital', lazy=True)

    def __repr__(self):
        return f"[{self.id},\t{self.name},\t{self.category},\t{self.city},\tDr. {self.doctors},\t{self.patients}]"

# -------USER MODEL-------------------------


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(32), unique=True, nullable=False)
    role = db.Column(db.String(32), nullable=False, default="Guest")
    password = db.Column(db.String(32), nullable=False)
    fullname = db.Column(db.String(32), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'),
                          nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'),
                           nullable=True)


def __repr__(self):
    return f"[{self.id},\t{self.login_name},\t{self.role},\t{self.password},\t{self.fullname},\t{self.doctor_id},\t{self.patient_id}]"

# -------DOCTOR MODEL-------------------------


class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='doctor',
                           lazy=True, uselist=False)
    designaton = db.Column(db.String(32))
    speciality = db.Column(db.String(32), nullable=False)
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'),
                            nullable=False)
    visits = db.relationship('Visit', backref='doctor',
                             lazy=True)

    def __repr__(self):
        return f"[{self.id},\t{self.user.fullname},\t{self.designaton},\t{self.speciality},\t{self.hospital_id},\t{len(self.visits)}]"

# -------PATIENT MODEL-------------------------


class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='patient',
                           lazy=True, uselist=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospital.id'),
                            nullable=False)
    visits = db.relationship('Visit', backref='patient',
                             lazy=True)

    def __repr__(self):
        return f"[{self.id},\t{self.user},\t{self.age},\t{self.gender},\t{self.hospital_id},\t{len(self.visits)}]"


# -------VISIT MODEL-------------------------

class Visit(db.Model):
    __tablename__ = "visit"
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'),
                          nullable=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'),
                           nullable=True)
    prescription = db.Column(db.Text, nullable=False)
    appointment_status = db.Column(db.String(10), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __repr__(self):
        return f"[{self.id},\t{self.doctor_id},\t{self.patient_id},\t{self.prescription},\t{self.appointment_status},\t{self.timestamp}]"


# ------------------For serializing the above Model objects-----------------------------------------

class HospitalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hospital
        include_relationships = True
        load_instance = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True


class DoctorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Doctor
        include_relationships = True
        load_instance = True


class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient
        include_relationships = True
        load_instance = True


class VisitSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Visit
        include_relationships = True
        load_instance = True
