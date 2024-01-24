from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import mapped_column

from server.core.base_model import BaseModel


class Operation(BaseModel):
    __tablename__ = "operation"

    id = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    left = mapped_column(Float, nullable=False)
    right = mapped_column(Float, nullable=False)
    result = mapped_column(Float, nullable=False)
    operation = mapped_column(String(length=320), nullable=False)
