from fastapi import FastAPI

from app.database.db import engine, Base
from app.models.employee import Employee
from app.routers.employee_routes import router as employee_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    description="FastAPI backend connected to PostgreSQL using SQLAlchemy",
    version="1.0.0"
)

app.include_router(employee_router)


@app.get("/")
def health_check():
    return {
        "message": "Employee Management API is running"
    }