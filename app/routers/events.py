from fastapi import APIRouter,Depends,HTTPException,status
from sqlmodel import Session,select

from app.db import get_session
from app.models import CareEvent,Elder

router = APIRouter(
    prefix="/events",
    tags=["care-events"]
)

@router.post("/",response_model=CareEvent,status_code=status.HTTP_201_CREATED)
def create_event(event:CareEvent,session:Session=Depends(get_session)):
    elder = session.get(Elder,event.elder_id)
    if not elder:
        raise HTTPException(
            status_code=404,
            detail="Elder not found",
        )

    session.add(event)
    session.commit()
    session.refresh(event)

    return event

@router.get(
    "/elder/{elder_id}",
    response_model=list[CareEvent],
)
def get_elder_events(
    elder_id: int,
    session: Session = Depends(get_session),
):
    elder = session.get(Elder, elder_id)

    if not elder:
        raise HTTPException(
            status_code=404,
            detail="Elder not found",
        )

    statement = (
        select(CareEvent)
        .where(CareEvent.elder_id == elder_id)
        .order_by(CareEvent.created_at.desc())
    )

    return session.exec(statement).all()