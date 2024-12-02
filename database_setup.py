from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URI = "sqlite:///fraud_detection.db"  

def create_database():
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas exitosamente.")

def get_session():
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    return Session()