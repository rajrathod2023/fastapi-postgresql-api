from fastapi import FastAPI

from app.database.db import engine, Base
from app.models.employee import Employee
from app.routers.employee_routes import router as employee_router

# Create database tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI(
    title="Employee Management API",
    description="FastAPI backend connected to PostgreSQL using SQLAlchemy",
    version="1.0.0"
)

# Routers
app.include_router(employee_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }

# Health endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }