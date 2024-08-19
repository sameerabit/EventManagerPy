from sqlalchemy.orm import Session
from . import models, schemas

def create_event(db: Session, event: schemas.EventCreate):
    db_event = models.Event(user_id=event.user_id, event_type=event.event_type)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
