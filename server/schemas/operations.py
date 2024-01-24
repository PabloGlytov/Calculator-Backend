from pydantic import BaseModel

from server.enums.operations_enum import Operations


class OperationCreate(BaseModel):
    left: float
    right: float
    operation: Operations
