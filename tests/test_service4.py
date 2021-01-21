from flask import url_for
from flask_testing import TestCase
from service4.app import app



class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestResponse(TestBase):
    # Test lucky day with base luck of 20, improved to 30 to achieve the worst fortune
    def test_fortune1(self):
        response = self.client.post(url_for('getfortune'), json={"day" : "7", "luck" : 20})
        print(response)
        self.assertIn(b'You are truly unlucky, the system predicts a bad event shall besiege your life soon, be careful!', response.data)
    # Test luck of 65
    def test_fortune2(self):
        response = self.client.post(url_for('getfortune'), json={"day" : "31", "luck" : 55})
        print(response)
        self.assertIn(b'You are lucky nor unlucky, perhaps a dark future awaits, perhaps not', response.data)
    # Test luck of 85
    def test_fortune3(self):
        response = self.client.post(url_for('getfortune'), json={"day" : "31", "luck" : 75})
        print(response)
        self.assertIn(b'You are a lucky individual, the gods have favoured your path and await good results', response.data)
    #Test luck of 110
    def test_fortune4(self):
        response = self.client.post(url_for('getfortune'), json={"day" : "2", "luck" : 130})
        print(response)
        self.assertIn(b'You are the luckiest individual on earth, Your past, present and future has been blessed by higher powers the system predicts a lottery win in the near future', response.data)
