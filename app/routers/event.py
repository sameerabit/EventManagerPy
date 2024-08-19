from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, controller, database

router = APIRouter()

@router.post("/submit_event")
def submit_event(event: schemas.EventCreate, db: Session = Depends(database.get_db)):
    return controller.create_event(db=db, event=event)
