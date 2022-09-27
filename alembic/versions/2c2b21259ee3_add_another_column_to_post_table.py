"""add another column to post table

Revision ID: 2c2b21259ee3
Revises: 3d818162e139
Create Date: 2022-09-27 19:37:04.947088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c2b21259ee3'
down_revision = '3d818162e139'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content',sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
