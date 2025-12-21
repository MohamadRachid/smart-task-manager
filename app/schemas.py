from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    deadline: datetime

class TaskResponse(BaseModel):
    id: int
    title: str
    deadline: datetime
    priority: str
    created_at: datetime

    class Config:
        orm_mode = True
