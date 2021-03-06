"""empty message

Revision ID: 33190c5ef504
Revises: 1e6456c834b4
Create Date: 2018-12-28 11:48:03.444134

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '33190c5ef504'
down_revision = '1e6456c834b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teacher', 'tage',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teacher', 'tage',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    # ### end Alembic commands ###
