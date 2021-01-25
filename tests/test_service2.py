from flask_testing import TestCase
from unittest.mock import patch
from flask import url_for
from service2.app import app
from random import choice, randint


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
years = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033"]
totalcomb = 12 * 12


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def testyearmon(self):
            with patch("random.choice") as random2:
                random2.side_effect = ["January", "2022"]
                response = self.client.get(url_for('getyearmon'))
                self.assertIn(b'January', response.data)
    

        
