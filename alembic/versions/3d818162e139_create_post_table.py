"""create post table

Revision ID: 3d818162e139
Revises: 
Create Date: 2022-09-07 21:12:23.857798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d818162e139'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",     sa.Integer(), nullable = False, primary_key= True),
                            sa.Column("title",  sa.String() , nullable = False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
