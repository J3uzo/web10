from sqlalchemy import Column, Integer, String
from ..database import Base

class Customer(Base):
    __tablename__ = "customers"

    Customer_id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    Email = Column(String(100))
    Number = Column(String(20))
    Company = Column(String(100))
    Post = Column(String(50))
    Tag = Column(String(50))