from sqlmodel import Session, select

from app.db import engine
from app.models import Elder, Medication


def get_medications(elder_id: int) -> list[dict]:
    """
    Fetch all medications for the elder.
    The application supplies elder_id.
    """

    with Session(engine) as session:
        elder = session.get(Elder, elder_id)

        if not elder:
            return []

        statement = (
            select(Medication)
            .where(Medication.elder_id == elder_id)
            .order_by(Medication.id)
        )

        medications = session.exec(statement).all()

        return [
            {
                "id": medication.id,
                "name": medication.name,
                "dosage": medication.dosage,
                "schedule": medication.schedule,
                "notes": medication.notes,
            }
            for medication in medications
        ]