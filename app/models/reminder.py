from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Reminder(Base):
    __tablename__ = "reminders"

    Reminder_id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    Description = Column(String(255))
    Date = Column(DateTime)
    Type = Column(String(50))
    Contact = Column(String(100))
    Customer_id = Column(Integer, ForeignKey("customers.Customer_id"))

    customer = relationship("Customer")