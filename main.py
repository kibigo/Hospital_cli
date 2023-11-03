from sqlalchemy import (
    String,
    Integer,
    Column,
    create_engine,
    ForeignKey,
    DateTime,
    func,
    Table
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import(
    relationship,
    sessionmaker
)



Base = declarative_base()

engine = create_engine('sqlite:///hospital.db')

ward_table = Table(
    'ward_table',
    Base.metadata,
    Column('patient_id', ForeignKey('patients.id')),
    Column('nurse_id', ForeignKey('nurses.id')),
    Column('doctor_id', ForeignKey('doctors.id'))
)

class Doctor (Base):
    __tablename__ = 'doctors'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    specialization = Column(String(), nullable=False)
    patient = relationship('Patient', backref='doctors')

    def __repr__(self):
        return f"Doctor name: {self.name}\
            Specialization: {self.specialization}"
    

class Nurse(Base):
    __tablename__ = 'nurses'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    shift = Column(String(), nullable=False)


    def __repr__(self):
        return f"Nurse name: {self.name}\
            Shift: {self.shift}"
    

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    disease = Column(String(), nullable=False)
    arrival_time = Column(DateTime, default=func.now)
    assigned_doctor= Column(Integer, ForeignKey('doctors.id'))
    

    def __repr__(self):
        return f"Patient name: {self.name}\
            disease: {self.disease}\
            arrival time: {self.arrival_time}"
    

Base.metadata.create_all(engine)

session = sessionmaker()(bind = engine)