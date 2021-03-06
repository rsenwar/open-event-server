"""empty message

Revision ID: 17881794fc87
Revises: b20ae211b8e0
Create Date: 2016-06-23 05:27:39.443032

"""

# revision identifiers, used by Alembic.
revision = '17881794fc87'
down_revision = 'b20ae211b8e0'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('max_order', sa.Integer(), nullable=True))
    op.add_column('ticket', sa.Column('min_order', sa.Integer(), nullable=True))
    op.add_column('ticket', sa.Column('sales_end', sa.DateTime(), nullable=False))
    op.add_column('ticket', sa.Column('sales_start', sa.DateTime(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'sales_start')
    op.drop_column('ticket', 'sales_end')
    op.drop_column('ticket', 'min_order')
    op.drop_column('ticket', 'max_order')
    ### end Alembic commands ###
