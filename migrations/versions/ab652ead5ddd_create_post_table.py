"""create post table

Revision ID: ab652ead5ddd
Revises: 59628dea39ff
Create Date: 2024-07-06 16:44:49.703007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab652ead5ddd'
down_revision = '59628dea39ff'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("post",
                    sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column("content", sa.Unicode(length=255), nullable=False),
                    sa.Column("title", sa.Unicode(length=255), nullable=False)
                    )


def downgrade():
    op.drop_table("post")

