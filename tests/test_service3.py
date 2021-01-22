from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from service3.app import app
from random import randint


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def testlucktrue(self):
        with patch("random.randint") as random:
            random.side_effect = [5,5]
            response = self.client.get(url_for('getluck'))
            self.assertEqual(b'True', response.data)

    def testluckfalse(self):
        with patch("random.randint") as random2:
            random2.side_effect = [1,6]
            response = self.client.get(url_for('getluck'))
            self.assertEqual(b'False', response.data)
    