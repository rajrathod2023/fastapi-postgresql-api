from fastapi import FastAPI

from app.routers.employee_routes import router as employee_router

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