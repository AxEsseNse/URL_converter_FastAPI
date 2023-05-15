from unittest import TestCase, main
from service import Service
from DataBase import SessionLocal
from uuid import uuid4

class CheckFeedback(TestCase):
    def test_msg_in_DB(self):
        self.assertEqual(Service.check_feedback(user_msg="красава", db=SessionLocal()).date,
                         1683912791.189309)

    def test_msg_not_in_DB(self):
        self.assertEqual(Service.check_feedback(user_msg=str(uuid4()), db=SessionLocal()),
                         None)


if __name__ == '__main__':
    main()
