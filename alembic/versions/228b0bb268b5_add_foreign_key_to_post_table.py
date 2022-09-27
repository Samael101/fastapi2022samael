"""add foreign-key to post table

Revision ID: 228b0bb268b5
Revises: 74bb3d75f613
Create Date: 2022-09-27 19:52:00.012478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '228b0bb268b5'
down_revision = '74bb3d75f613'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('owner_id',sa.Integer(),nullable= False))
    op.create_foreign_key("post_users_FK", source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_FK', table_name='posts')
    op.drop_column('posts','ower_id')
    pass
