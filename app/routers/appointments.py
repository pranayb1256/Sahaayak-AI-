from datetime import datetime,timezone

from fastapi import APIRouter, Depends, HTTPException,status
from sqlmodel import Session, select

from app.db import get_session
from app.models import Appointment,Elder

router = APIRouter(prefix="/appointments",tags=["appointments"])

@router.post("/",response_model=Appointment,status_code=status.HTTP_201_CREATED)
def create_appointment(appointment:Appointment, session:Session=Depends(get_session)):
    elder = session.get(Elder,appointment.elder_id)
    if not elder:
        raise HTTPException(
            status_code=404,
            detail="Elder not Found"
        )
    if isinstance(appointment.datetime, str):
        appointment.datetime = datetime.fromisoformat(appointment.datetime)
    session.add(appointment)
    session.commit()
    session.refresh(appointment)
    
    return appointment

@router.get("/elder/{elder_id}",response_model=list[Appointment])
def get_elder_appointments(elder_id:int,session:Session=Depends(get_session)):
    elder = session.get(Elder,elder_id)
    if not elder:
        raise HTTPException(
            status_code=404,
            detail="Elder not found",
        )
    stmt = (
        select(Appointment)
        .where(Appointment.elder_id == elder_id)
        .order_by(Appointment.datetime)
    )
    return session.exec(stmt).all()



@router.get("/elder/{elder_id}/upcoming",response_model=list[Appointment])
def get_upcoming_appointments(elder_id:int,session:Session=Depends(get_session)):
    elder = session.get(Elder,elder_id)
    
    if not elder:
        raise HTTPException(
            status_code=404,
            detail="Elder not Found"
        )
        
    now = datetime.now(timezone.utc)
    statement = (
        select(Appointment)
        .where(
            Appointment.elder_id == elder_id,
            Appointment.datetime >= now,
        )
        .order_by(Appointment.datetime)
    )

    return session.exec(statement).all()

















