import os
from alembic.config import Config
from alembic import command
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas import CreateJobRequest
from src.database import get_db
from src.models import Job


current_dir = os.path.dirname(os.path.realpath(__file__))
alembic_cfg = Config(f"{current_dir}/alembic.ini")
alembic_cfg.set_main_option('sqlalchemy.url', os.getenv('CONNECTION_STRING', 'postgresql://postgres:mysuperpassword@localhost/youtube'))
command.upgrade(alembic_cfg, "head")

app = FastAPI()

@app.post("/")
def create(details: CreateJobRequest, db: Session = Depends(get_db)):
    to_create = Job(
        title=details.title,
        description=details.description
    )
    db.add(to_create)
    db.commit()
    return { 
        "success": True,
        "created_id": to_create.id
    }

@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()

@app.delete("/")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Job).filter(Job.id == id).delete()
    db.commit()
    return { "success": True }
