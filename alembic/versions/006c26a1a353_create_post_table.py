"""create post table

Revision ID: 006c26a1a353
Revises: 
Create Date: 2022-12-20 14:19:39.085655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '006c26a1a353'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts", sa.Column(
            "id", sa.Integer(), nullable=False, 
            primary_key=True), sa.Column("title", sa.String(), nullable=False))              
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
