import json

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from server.db_services.operations_db_service import OperationsDBService
from server.schemas.operations import OperationCreate


class OperationsService:
    async def create_calculation(new_operation: OperationCreate, session: AsyncSession):
        try:
            data = await OperationsDBService().create(new_operation, session)
            return {"status": "success", "data": data, "message": "New calculation"}
        except ZeroDivisionError as e:
            raise HTTPException(
                status_code=500,
                detail={
                    "status": "error",
                    "data": None,
                    "message": "You can't divide by zero",
                },
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail={
                    "status": "error",
                    "data": None,
                    "message": "Something wrong : (",
                },
            )
