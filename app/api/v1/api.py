from fastapi import APIRouter

from app.api.v1.routers.auth import router as auth_router
from app.api.v1.routers.piggy import router as piggy_router
from app.api.v1.routers.transactions import router as transactions_router

version="v1"

pb_router = APIRouter()

pb_router.include_router(auth_router)
pb_router.include_router(piggy_router)
pb_router.include_router(transactions_router)