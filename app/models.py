from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    Author = Column(String,index=True)
    Publication_Date = Column(DateTime,index=True)
    ISBN = Column(Integer,index=True)
    Cover_Image = Column(String,index=True)

