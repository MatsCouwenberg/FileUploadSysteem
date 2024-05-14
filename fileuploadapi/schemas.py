from pydantic import BaseModel, Field
from datetime import datetime

# Schema for creating a new file
class FileCreate(BaseModel):
    filename: str
    path: str
    username: str

    class Config:
        arbitrary_types_allowed = True

# Schema for returning file information
class File(FileCreate):
    id: int
    created_at: datetime