from fastapi import APIRouter, Depends,HTTPException,status
from sqlmodel import Session, select
from websockets import route

from app.db import get_session
from app.models import Medication,Elder

router = APIRouter(prefix="/medications",tags=["medications"])

@router.post("/",response_model=Medication,status_code=status.HTTP_201_CREATED)
def create_medication(medication:Medication,session:Session=Depends(get_session)):
    elder = session.get(Elder,medication.elder_id)
    if not elder:
        raise HTTPException(status_code=404,detail="Elder not Found")
    session.add(medication)
    session.commit()
    session.refresh(medication)
    return medication

@router.get("/elder/{elder_id}",response_model=list[Medication])
def get_elder_medications(elder_id:int,session:Session=Depends(get_session)):
    elder = session.get(Elder,elder_id)
    if not elder:
        raise HTTPException(status_code=404,detail="Elder not Found")
    stmt = select(Medication).where(Medication.elder_id==elder_id)
    results=session.exec(stmt).all()
    return results