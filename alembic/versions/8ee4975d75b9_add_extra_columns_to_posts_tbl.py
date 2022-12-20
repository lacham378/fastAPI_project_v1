"""add extra_columns to posts_tbl

Revision ID: 8ee4975d75b9
Revises: 9003dd422687
Create Date: 2022-12-20 16:43:19.332516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ee4975d75b9'
down_revision = '9003dd422687'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('published', sa.Boolean(), 
                            nullable=False, 
                            server_default='TRUE'),)
    
    op.add_column('posts',
                  sa.Column('created_at', 
                            sa.TIMESTAMP(timezone=True), 
                            nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
