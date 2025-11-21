from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from ..database import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    customer_id = Column(Integer, ForeignKey("customers.Customer_id"))
    quantity = Column(Integer, default=1)
    purchase_date = Column(DateTime)

    item = relationship("Item")
    customer = relationship("Customer")

    