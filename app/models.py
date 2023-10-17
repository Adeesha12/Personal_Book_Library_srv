from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_utils import PasswordType, EmailType
from database import Base


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    Author = Column(String,index=True)
    Publication_Date = Column(DateTime,index=True)
    ISBN = Column(Integer,index=True)
    Cover_Image = Column(String,index=True)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True, index=True)
    fullname = Column(String,index=True)
    email = Column(EmailType,index=True)
    password = Column(PasswordType(schemes=['pbkdf2_sha512','md5_crypt'],deprecated=['md5_crypt']),index=True)