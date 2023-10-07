from fastapi import APIRouter, HTTPException, Depends
from typing import List
from model import BookItem
from auth.jwt_bearer import JWTBearer

books_router = APIRouter(
    prefix="/v1/books",
    tags=["books"]
)


books = []

@books_router.get("/books", dependencies=[Depends(JWTBearer())], response_model=List[BookItem])
def get_books():
    return books

@books_router.get("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def get_books(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    return books[book_id]

@books_router.post("/books", response_model=BookItem)
def create_books(book: BookItem):
    books.append(book)
    return book

@books_router.put("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def update_books(book_id: int , book: BookItem):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    books[book_id] = book
    return book

@books_router.delete("/books/{book_id}", dependencies=[Depends(JWTBearer())], response_model=BookItem)
def delete_books(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    delete_book = books.pop(book_id)
    return delete_book


