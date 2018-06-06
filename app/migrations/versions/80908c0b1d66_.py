"""empty message

Revision ID: 80908c0b1d66
Revises: 39d187ca3816
Create Date: 2018-06-06 15:30:03.070062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80908c0b1d66'
down_revision = '39d187ca3816'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first', sa.String(length=30), nullable=True))
    op.add_column('user', sa.Column('last', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last')
    op.drop_column('user', 'first')
    # ### end Alembic commands ###