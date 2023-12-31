import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from sqlalchemy.exc import OperationalError
import time

from database import engine
import models
from routes.books import books_router
from routes.auth import register_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(books_router)
app.include_router(register_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4)