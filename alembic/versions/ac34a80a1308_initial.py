"""initial

Revision ID: ac34a80a1308
Revises: 9f5aa5fc2178
Create Date: 2022-11-22 18:54:26.827131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac34a80a1308'
down_revision = '9f5aa5fc2178'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'category_code',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('items', 'category_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('items', 'subcategori_code',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('items', 'subcategori_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('items', 'subcategori_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('items', 'subcategori_code',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('items', 'category_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('items', 'category_code',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###
