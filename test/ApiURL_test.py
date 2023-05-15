from unittest import TestCase, main
from service import Service
from DataBase import SessionLocal


class CheckUrl(TestCase):
    def test_url_in_DB(self):
        self.assertEqual(Service.check_url(user_url="https://www.youtube.com/", db=SessionLocal()).short_url,
                         "PkUOE")

    def test_url_not_in_DB(self):
        self.assertEqual(Service.check_url(user_url="https://www.yofast53626ssfaszxz32cfasabe.com/", db=SessionLocal()),
                         None)


class CheckShortUrl(TestCase):
    def test_short_url_in_DB(self):
        self.assertEqual(Service.check_short_url(user_short_url="PkUOE", db=SessionLocal()).url,
                         "https://www.youtube.com/")

    def test_short_url_not_in_DB(self):
        self.assertEqual(Service.check_short_url(user_short_url="AAAA", db=SessionLocal()),
                         None)


if __name__ == '__main__':
    main()
