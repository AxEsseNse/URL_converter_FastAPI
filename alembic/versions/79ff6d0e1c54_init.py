"""init. Create url, feedback tables

Revision ID: 79ff6d0e1c54
Revises: 
Create Date: 2023-05-15 14:59:45.824520

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '79ff6d0e1c54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('url',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('short_url', sa.String(5), unique=True),
                    sa.Column('url', sa.String(), unique=True),
                    sa.Column('date_creating', sa.Float(), default=datetime.timestamp(datetime.utcnow())),
                    sa.Column('count_use', sa.Integer(), default=1),
                    sa.Column('date_last_use', sa.Float(), default=datetime.timestamp(datetime.utcnow()))
                    )
    op.create_table('feedback',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('msg', sa.String(250), unique=True),
                    sa.Column('date', sa.Float(), default=datetime.timestamp(datetime.utcnow()))
                    )


def downgrade() -> None:
    op.drop_table('url')
    op.drop_table('feedback')
