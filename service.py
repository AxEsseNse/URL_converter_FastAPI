from sqlalchemy.orm import Session
from DBModel.model import ModelURL, ModelFeedback
from Scheme.url import URLBase


def get_url(db: Session):
    return db.query(ModelURL).first()


def create_url(db: Session, url: URLBase):
    url = ModelURL(**url.dict())
    db.add(url)
    db.commit()
    db.refresh(url)
    return url
