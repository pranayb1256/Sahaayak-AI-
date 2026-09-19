from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Elder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None
    preferred_language: Optional[str] = "Hi"
    notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


class Medication(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    elder_id: int = Field(foreign_key="elder.id")
    name: str
    dosage: Optional[str] = None
    schedule: Optional[str] = None
    notes: Optional[str] = None


class Appointment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    elder_id: int = Field(foreign_key="elder.id")
    title: str
    datetime: datetime
    location: Optional[str] = None
    doctor: Optional[str] = None
    notes: Optional[str] = None


class CareEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    elder_id: int = Field(foreign_key="elder.id")
    event_type: str  # e.g. "symptom", "missed_med", "checkin"
    details: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)