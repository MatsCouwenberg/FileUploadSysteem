from sqlalchemy.orm import Session
import models
import schemas

def create_file(db: Session, file_info: schemas.FileCreate):
    db_file = models.File(**file_info.dict())
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_files(db: Session):
    return db.query(models.File).all()