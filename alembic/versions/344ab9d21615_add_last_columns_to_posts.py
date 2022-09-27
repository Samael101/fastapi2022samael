"""add last columns to posts

Revision ID: 344ab9d21615
Revises: 228b0bb268b5
Create Date: 2022-09-27 20:30:49.911882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '344ab9d21615'
down_revision = '228b0bb268b5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('published',sa.Boolean(),nullable= False, server_default="True"))
    op.add_column("posts", sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable= False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
    pass
