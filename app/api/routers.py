from fastapi import APIRouter
from .endpoints import role, user, faculty, department, division, employees

api_router = APIRouter()
api_router.include_router(role.router, tags=["roles"])
api_router.include_router(user.router, tags=["users"])
api_router.include_router(faculty.router, tags=["faculties"])
api_router.include_router(department.router, tags=["departments"])
api_router.include_router(division.router, tags=["divisions"])
api_router.include_router(employees.router, tags=["employees"])
