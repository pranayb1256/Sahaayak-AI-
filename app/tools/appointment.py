from datetime import datetime

from sqlmodel import Session, select

from app.db import engine
from app.models import Appointment, Elder


def get_upcoming_appointments(elder_id: int) -> list[dict]:
    """
    Get upcoming appointments for the elder controlled
    by the application.
    """

    with Session(engine) as session:
        elder = session.get(Elder, elder_id)

        if not elder:
            return []

        now = datetime.utcnow()

        statement = (
            select(Appointment)
            .where(
                Appointment.elder_id == elder_id,
                Appointment.datetime >= now,
            )
            .order_by(Appointment.datetime)
        )

        appointments = session.exec(statement).all()

        return [
            {
                "id": appointment.id,
                "title": appointment.title,
                "datetime": (
                    appointment.datetime.isoformat()
                    if appointment.datetime
                    else None
                ),
                "location": appointment.location,
                "doctor": appointment.doctor,
                "notes": appointment.notes,
            }
            for appointment in appointments
        ]