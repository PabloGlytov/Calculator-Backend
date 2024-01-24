"""empty message

Revision ID: a7624b6c9213
Revises: f00524b28ca2
Create Date: 2024-01-21 10:14:11.174847

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a7624b6c9213"
down_revision: Union[str, None] = "f00524b28ca2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("operation", sa.Column("right", sa.Float(), nullable=False))
    op.add_column("operation", sa.Column("result", sa.Float(), nullable=False))
    op.add_column(
        "operation", sa.Column("operation", sa.String(length=320), nullable=False)
    )
    op.create_unique_constraint(None, "operation", ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "operation", type_="unique")
    op.drop_column("operation", "operation")
    op.drop_column("operation", "result")
    op.drop_column("operation", "right")
    # ### end Alembic commands ###
