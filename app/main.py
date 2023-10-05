from fastapi import FastAPI, HTTPException
from typing import List, Optional
from model import BookItem

app = FastAPI()

books = []

@app.get("/books", response_model=List[BookItem])
def get_books():
    return books

@app.post("/books", response_model=BookItem)
def create_books(book: BookItem):
    books.append(book)
    return book

@app.put("/books/{book_id}", response_model=BookItem)
def update_books(book_id: int , book: BookItem):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    books[book_id] = book
    return book

@app.delete("/books/{book_id}" ,response_model=BookItem)
def delete_books(book_id: int):
    if book_id < 0 or book_id >= len(books):
        raise HTTPException(status_code=404, detail="book not found")
    delete_book = books.pop(book_id)
    return delete_book
    