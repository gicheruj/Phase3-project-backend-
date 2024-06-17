from sqlalchemy import Column, Integer, String
from database import Base

class FormData(Base):
    __tablename__ = "formdata"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    email = Column(String, index=True)
    company = Column(String, index=True)
    amount = Column(Integer)
    hospital = Column(String, index=True)
    county = Column(String, index=True)
