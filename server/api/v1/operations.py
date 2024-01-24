from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from server.core.db import get_session
from server.schemas.operations import OperationCreate
from server.services.operations_service import OperationsService

router = APIRouter(prefix="/calculation", tags=["calculation"])


@router.post("/calculate/")
async def calculate(
    operation_data: OperationCreate, session: AsyncSession = Depends(get_session)
):
    return await OperationsService.create_calculation(operation_data, session)
