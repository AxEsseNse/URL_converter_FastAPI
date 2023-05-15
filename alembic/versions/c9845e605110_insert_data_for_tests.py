"""insert data for tests

Revision ID: c9845e605110
Revises: 79ff6d0e1c54
Create Date: 2023-05-15 15:32:30.316129

"""
from DataBase import SessionLocal
from DBModel.model import ModelURL, ModelFeedback


# revision identifiers, used by Alembic.
revision = 'c9845e605110'
down_revision = '79ff6d0e1c54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    db = SessionLocal()
    test_data_url = ModelURL(url='test', short_url='test')
    db.add(test_data_url)
    test_data_feedback = ModelFeedback(msg='test')
    db.add(test_data_feedback)
    db.commit()
    db.close()


def downgrade() -> None:
    db = SessionLocal()
    db.query(ModelURL).filter_by(short_url='test').delete()
    db.query(ModelFeedback).filter_by(msg='test').delete()
    db.commit()
    db.close()
