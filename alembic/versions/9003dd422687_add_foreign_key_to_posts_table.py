"""add foreign-key to posts table

Revision ID: 9003dd422687
Revises: fa37868d3a86
Create Date: 2022-12-20 16:25:49.262812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9003dd422687'
down_revision = 'fa37868d3a86'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', 
                          referent_table='users', 
                          local_cols=['owner_id'], 
                          remote_cols=['id'], 
                          ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
