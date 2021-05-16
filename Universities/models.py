from typing import Optional

from passlib.context import CryptContext
from sqlalchemy import Column, Integer,String,Boolean

from Universities.database import Base


class UniversitiesList(Base):
    __tablename__='Universities'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    country=Column(String)

class Users(Base):
    __tablename__='Users'
    id = Column(Integer, primary_key=True, index=True)
    email=Column(String)
    password=Column(String)
    full_name=Column(String)
    disabled=Column(Boolean)



class Universities(Base):
    __tablename__ = 'UniversitiesDetailed'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    country = Column(String)
    description = Column(String)
    Alt_Name = Column(String)
    Acronym = Column(String)
    Founded = Column(String)
    Colours = Column(String)
    Screenshot = Column(String)
    Address = Column(String)
    Tel = Column(String)
    Fax = Column(String)
    Other_locations = Column(String)
    Gender = Column(String)
    International_Students = Column(String)
    Selection_Type = Column(String)
    Admission_Rate = Column(String)
    Admission_Office = Column(String)
    Student_Enrollment = Column(String)
    Academic_Staff = Column(String)
    Control_Type = Column(String)
    Entity_Type = Column(String)
    Academic_Calendar = Column(String)
    Campus_Setting = Column(String)
    Religious_Affiliation = Column(String)
    Basic_Classification = Column(String)
    Classification = Column(String)
    Size_Setting = Column(String)
    Enrollment_Profile = Column(String)
    Undergraduate_Profile = Column(String)
    Undergraduate_Instructional_Program = Column(String)
    Graduate_Instructional_Program = Column(String)
    Library = Column(String)
    Housing = Column(String)
    Sport_Facilities = Column(String)
    Financial_Aids = Column(String)
    Study_Abroad = Column(String)
    Distance_Learning = Column(String)
    Academic_Counseling = Column(String)
    Career_Services = Column(String)
    Institutional_Hospital = Column(String)
    Motto = Column(String)
    New_Admission_Requirements = Column(String)
    Minority_Serving = Column(String)
    Land_Grant_Institution = Column(String)

