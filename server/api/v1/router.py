from fastapi import APIRouter

from server.api.v1.operations import router as operations_router

router = APIRouter(prefix="/v1")

router.include_router(operations_router)
