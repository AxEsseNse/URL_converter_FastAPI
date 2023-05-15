from unittest import TestCase, main
from service import Service
from DataBase import SessionLocal
from uuid import uuid4
from DBModel.model import ModelURL


class CheckUrl(TestCase):
    def test_url_in_DB(self):
        self.assertEqual(Service.check_url(user_url="test", db=SessionLocal()).short_url,
                         "test")

    def test_url_not_in_DB(self):
        self.assertEqual(Service.check_url(user_url=str(uuid4()), db=SessionLocal()),
                         None)


class CheckShortUrl(TestCase):
    def test_short_url_in_DB(self):
        self.assertEqual(Service.check_short_url(user_short_url="test", db=SessionLocal()).url,
                         "test")

    def test_short_url_not_in_DB(self):
        self.assertEqual(Service.check_short_url(user_short_url="A", db=SessionLocal()),
                         None)


class UpdateUrlData(TestCase):
    def test_url_data_update(self):
        db = SessionLocal()
        url_data = db.query(ModelURL).filter_by(url="test").first()
        count_use = url_data.count_use
        self.assertEqual(Service.update_url_data(data=url_data, db=db),
                         count_use+1)


if __name__ == '__main__':
    main()
