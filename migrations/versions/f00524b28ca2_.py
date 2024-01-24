"""empty message

Revision ID: f00524b28ca2
Revises: 6b25aa7665cb
Create Date: 2024-01-21 14:12:43.165279

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f00524b28ca2"
down_revision: Union[str, None] = "6b25aa7665cb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "operation",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("left", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("operation")
    # ### end Alembic commands ###