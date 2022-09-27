"""add user table

Revision ID: 74bb3d75f613
Revises: 2c2b21259ee3
Create Date: 2022-09-27 19:42:40.621044

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74bb3d75f613'
down_revision = '2c2b21259ee3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", sa.Integer(), nullable = False),
        sa.Column("email", sa.String(), nullable = False),
        sa.Column("password", sa.String(), nullable = False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
        )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
