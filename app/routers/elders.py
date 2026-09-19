from fastapi import APIRouter,Depends,HTTPException,status
from sqlmodel import Session,select
from sqlalchemy import desc
from typing import List

from app.db import get_session
from app.models import Elder

router = APIRouter(prefix="/elders",tags=["elders"])

@router.post("/",response_model=Elder,status_code=status.HTTP_201_CREATED)
def create_elder(elder:Elder,session:Session=Depends(get_session)):
    db_elder = Elder(**elder.model_dump())
    session.add(db_elder)
    session.commit()
    session.refresh(db_elder)
    return db_elder

@router.get("/{elder_id}",response_model=Elder)
def read_elder(elder_id:int,session:Session = Depends(get_session)):
    elder = session.get(Elder,elder_id)
    if not elder:
        raise HTTPException(status_code=404,detail="Elder not Found")
    return elder

@router.get("/",response_model=List[Elder])
def list_elder(session:Session = Depends(get_session)):
    stmt = select(Elder).order_by(desc(Elder.created_at))
    results=session.exec(stmt).all()
    return results