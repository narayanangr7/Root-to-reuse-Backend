from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Volunteer(Base):
    __tablename__ = "volunteer"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    email = Column(String, nullable=False)
    phone_no = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    location = Column(String, nullable=False)
    message = Column(String,nullable=False)
    volunteer = relationship("User")
   

