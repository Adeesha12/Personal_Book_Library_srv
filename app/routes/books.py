from fastapi import APIRouter, HTTPException, Depends
from typing import List, Annotated
from sqlalchemy.orm import Session
from database import get_db
from schema import BookItem
from auth.jwt_bearer import JWTBearer
import models

books_router = APIRouter(
    prefix="/v1/books",
    tags=["books"]
)

db_dependancy = Annotated[Session, Depends(get_db)]
books = []

@books_router.get("/books", dependencies=[Depends(JWTBearer())], response_model=List[BookItem])
def get_books(db:db_dependancy):
    results = db.query(models.Books).all()
    return results

@books_router.get("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def get_books(book_id: int, db:db_dependancy):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    return books[book_id]

@books_router.post("/books", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def create_books(book: BookItem, db:db_dependancy):
    books.append(book)
    return book

@books_router.put("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def update_books(book_id: int , book: BookItem, db:db_dependancy):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    books[book_id] = book
    return book

@books_router.delete("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def delete_books(book_id: int, db:db_dependancy):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    delete_book = books.pop(book_id)
    return delete_book


