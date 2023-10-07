import uvicorn
from routes.books import books_router
from routes.auth import register_router
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from model import BookItem

app = FastAPI()
app.include_router(books_router)
app.include_router(register_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=2)