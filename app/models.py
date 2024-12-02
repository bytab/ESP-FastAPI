from sqlalchemy import Column, Integer, String, Text
from app.database import Base

# Item model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    manufacturer = Column(String, nullable=True)
    price = Column(String, nullable=True)
    additional_info = Column(Text, nullable=True)
