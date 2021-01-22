from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from service3.app import app
from random import  randint

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def testgetluck(self):
            with patch("random.randint") as random:
                random.return_value = 3
                response = self.client.get(url_for('getluck'))
                self.assertIn(b'3', response.data)
   