from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.database import Base

class Camp(Base):
    __tablename__ = "camp"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)

    volunteer_id = Column(Integer, ForeignKey("volunteer.id"), nullable=False)

    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    hours = Column(Integer, nullable=False)
    message = Column(Text, nullable=True)

    # relationship in volunteer.moduls  class Volunteer and back_popuates is a this table 
    camps = relationship("Volunteer")


 