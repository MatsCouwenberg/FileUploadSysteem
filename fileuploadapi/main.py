from fastapi import FastAPI, HTTPException, Depends, status, APIRouter, Request
from pydantic import BaseModel
from database import SessionLocal, Base, engine, Session
from models import *
from fastapi.middleware.cors import CORSMiddleware
import schemas
import crud
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Endpoint to upload file info
@app.post("/upload/", response_model=schemas.File)
def upload_file(file_info: schemas.FileCreate, db: Session = Depends(get_db)):
    return crud.create_file(db=db, file_info=file_info)

# Endpoint to get all entries
@app.get("/files/", response_model=List[schemas.File])
def get_files(db: Session = Depends(get_db)):
    return crud.get_files(db=db)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)