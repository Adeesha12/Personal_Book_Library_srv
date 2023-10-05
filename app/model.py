from pydantic import BaseModel 
from datetime import date

class BookItem(BaseModel):
    title: str
    Author: str
    Publication_Date: date  
    ISBN: int
    Cover_Image: str