from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from server.models.operation import Operation
from server.schemas.operations import OperationCreate


class OperationsDBService:
    """Service for manipulating Operation model"""

    table = Operation
    create_scheme = OperationCreate

    @classmethod
    async def create(
        cls,
        input_data: create_scheme,
        session: AsyncSession,
    ):
        params = input_data.model_dump()
        params["operation"] = params["operation"].value
        params["result"] = eval(
            f"{params['left']} {params['operation']} {params['right']}"
        )
        stmt = insert(cls.table).values(**params)
        await session.execute(stmt)
        await session.commit()
        return params
