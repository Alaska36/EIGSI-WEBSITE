from sqlalchemy import Column, ForeignKey, Integer, String, Text, DECIMAL
from sqlalchemy.orm import declarative_base, relationship
from app.database import Base




Base = declarative_base()





class UserWeb(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String)

    merchants = relationship("Merchant", back_populates="user")

class Merchant(Base):
    __tablename__ = 'merchants'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="merchants")
    products = relationship("Product", back_populates="merchant")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)  # Enlève la virgule ici
    price = Column(DECIMAL(10, 2), nullable=False)
    merchant_id = Column(Integer, ForeignKey('merchants.id'))

    merchant = relationship("Merchant", back_populates="products")