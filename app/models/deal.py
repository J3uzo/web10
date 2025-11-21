from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Deal(Base):
    __tablename__ = "deals"

    Deal_id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    Customer_id = Column(Integer, ForeignKey("customers.Customer_id"))
    Amount = Column(Float)
    Stage = Column(String(50))
    Probability = Column(Float)
    Date = Column(DateTime)
    Notes = Column(String(255))

    customer = relationship("Customer")