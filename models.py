from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    AccountID = Column(String(50), primary_key=True)
    CustomerAge = Column(Integer, nullable=False)
    CustomerOccupation = Column(String(100), nullable=False)
    AccountBalance = Column(Float, nullable=False)

class Transaction(Base):
    __tablename__ = "transactions"
    TransactionID = Column(String(50), primary_key=True)
    AccountID = Column(String(50), ForeignKey('accounts.AccountID'), nullable=False)
    TransactionAmount = Column(Float, nullable=False)
    TransactionDate = Column(DateTime, nullable=False)
    TransactionType = Column(String(20), nullable=False)
    Location = Column(String(100), nullable=False)
    DeviceID = Column(String(50), nullable=False)
    IPAddress = Column(String(50), nullable=False)
    MerchantID = Column(String(50), nullable=False)
    Channel = Column(String(50), nullable=False)
    Anomaly = Column(Boolean, nullable=False)
