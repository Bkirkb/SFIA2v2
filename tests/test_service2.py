from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from service2.app import app
from random import choice, randint


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def testmonth(self):
            with patch("random.choice") as random:
                random.return_value = "January"
                response = self.client.get(url_for('getday'))
                self.assertIn(b'January', response.data)

    def testmonth2(self):
            with patch("random.choice") as random:
                random.return_value = "April"
                response = self.client.get(url_for('getday'))
                self.assertIn(b'April', response.data)

    def testmonth3(self):
            with patch("random.choice") as random:
                random.return_value = "February"
                response = self.client.get(url_for('getday'))
                self.assertIn(b'February', response.data)

    def testday(self):
            with patch("random.randint") as random2:
                random2.return_value = 28
                response = self.client.get(url_for('getday'))
                self.assertIn(b'28', response.data)