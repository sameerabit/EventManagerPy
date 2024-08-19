from pydantic import BaseModel

class EventCreate(BaseModel):
    user_id: str
    event_type: str

    class Config:
        orm_mode = True