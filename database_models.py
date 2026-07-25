from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Float
Base = declarative_base()

class Product(Base):
    id = Column(Integer,primary_key=True, Index=True)
    name:str
    description:str
    price:float
    quantity:int
