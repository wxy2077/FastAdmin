"""modify field phone

Revision ID: a6563878a3ad
Revises: ed84d6b0b6f5
Create Date: 2020-07-07 16:59:26.404471

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a6563878a3ad'
down_revision = 'ed84d6b0b6f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_user', 'phone',
               existing_type=mysql.VARCHAR(length=16),
               nullable=True,
               existing_comment='手机号')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_user', 'phone',
               existing_type=mysql.VARCHAR(length=16),
               nullable=False,
               existing_comment='手机号')
    # ### end Alembic commands ###