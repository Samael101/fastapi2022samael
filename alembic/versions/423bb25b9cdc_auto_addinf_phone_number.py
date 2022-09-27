"""auto addinf phone Number

Revision ID: 423bb25b9cdc
Revises: 1ebbb8e0a5e2
Create Date: 2022-09-27 20:44:17.770684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '423bb25b9cdc'
down_revision = '1ebbb8e0a5e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
