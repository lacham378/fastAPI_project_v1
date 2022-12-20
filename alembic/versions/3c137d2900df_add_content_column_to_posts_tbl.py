"""add content column to posts_tbl

Revision ID: 3c137d2900df
Revises: 006c26a1a353
Create Date: 2022-12-20 15:31:20.230473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c137d2900df'
down_revision = '006c26a1a353'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
