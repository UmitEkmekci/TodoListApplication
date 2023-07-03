from sqlalchemy import Boolean, Column, Integer, String
from .database import Base # database.py dosyasında tanımlanan Base = declarative_base()
 
class Todo(Base):
    __tablename__ = "todos"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    
