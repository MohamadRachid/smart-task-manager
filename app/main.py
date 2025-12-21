from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from .database import SessionLocal, engine
from .models import Task, Base
from .schemas import TaskCreate, TaskResponse

app = FastAPI(title="Smart Task Manager")

# Create tables at startup
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def calculate_priority(deadline: datetime) -> str:
    now = datetime.utcnow()
    if deadline <= now + timedelta(hours=24):
        return "HIGH"
    elif deadline <= now + timedelta(days=3):
        return "MEDIUM"
    else:
        return "LOW"

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    priority = calculate_priority(task.deadline)
    db_task = Task(
        title=task.title,
        deadline=task.deadline,
        priority=priority
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()
