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
    book = db.query(models.Books).filter(models.Books.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return book
    # if book_id < 0 or book_id >= len(books):
    #     raise HTTPException(status_code=404, detail="book not found")
    # return books[book_id]

@books_router.post("/books", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def create_books(book: BookItem, db:db_dependancy):
    db_book = models.Books(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    db.close()
    return db_book


@books_router.put("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def update_books(book_id: int , book: BookItem, db:db_dependancy):
    db_book = db.query(models.Books).filter(models.Books.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for field, value in book.model_dump().items():
        setattr(db_book, field, value)

    db.commit()
    db.refresh(db_book)
    return db_book
    
    # if book_id < 0 or book_id >= len(books):
    #     raise HTTPException(status_code=404, detail="book not found")
    # books[book_id] = book
    # return book

@books_router.delete("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def delete_books(book_id: int, db:db_dependancy):
    db_book = db.query(models.Books).filter(models.Books.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_book)
    db.commit()
    return db_book

    # if book_id < 0 or book_id >= len(books):
    #     raise HTTPException(status_code=404, detail="book not found")
    # delete_book = books.pop(book_id)
    # return delete_book


