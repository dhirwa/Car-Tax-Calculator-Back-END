"""empty message

Revision ID: b423dd3068f5
Revises: dab938ac5a64
Create Date: 2016-11-09 17:00:15.074103

"""

# revision identifiers, used by Alembic.
revision = 'b423dd3068f5'
down_revision = 'dab938ac5a64'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('cr_id', sa.Integer(), nullable=False),
    sa.Column('cr_brand', sa.String(length=50), nullable=True),
    sa.Column('cr_mark', sa.String(length=50), nullable=True),
    sa.Column('cr_engine', sa.String(length=50), nullable=True),
    sa.Column('cr_drive', sa.String(length=50), nullable=True),
    sa.Column('cr_year', sa.Integer(), nullable=True),
    sa.Column('cr_newprice', sa.Integer(), nullable=True),
    sa.Column('cr_body', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('cr_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cars')
    ### end Alembic commands ###
