from fastapi import FastAPI
from app.db import create_db_and_tables
from contextlib import asynccontextmanager
from app.routers import (
    elders,
    medications,
    appointments,
    events,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
app=FastAPI(
    title="Sahaayak AI",
    description="AI Powered elder-care coordinator for Indian Families",
    version="0.1.0",
    lifespan=lifespan
)
app.router.lifespan_context(lifespan)
app.include_router(elders.router)
app.include_router(medications.router)
app.include_router(appointments.router)
app.include_router(events.router)
@app.get("/")
def root():
    return {
        "message":"Sahaayak AI is running",
        "status":"ok",
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy",
    }
