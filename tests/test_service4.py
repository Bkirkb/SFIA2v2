from flask import url_for
from flask_testing import TestCase
from service4.app import app



class TestBase(TestCase):
    def create_app(self):
        return app
    
class TestResponse(TestBase):
    # Test unlucky year but double dice
    def test_fortune1(self):
        response = self.client.post(url_for('getfortune'), json={"year" : "2021", "luck" : "True"})
        print(response)
        self.assertIn(b'Though you may be skilled with the dice, you should avoid danger in your chosen year', response.data)
    # Test lucky year and double dice
    def test_fortune2(self):
        response = self.client.post(url_for('getfortune'), json={"year" : "2022", "luck" : "True"})
        print(response)
        self.assertIn(b'You\'ve rolled a double in the game and in life, you are truly lucky', response.data)
    #Test lucky year and not double dice
    def test_fortune3(self):
        response = self.client.post(url_for('getfortune'), json={"year" : "2022", "luck" : "False"})
        print(response)
        self.assertIn(b'Your luck is not with the dice rolls, but your future is bright', response.data)
    # Test neutral year and double dice
    def test_fortune4(self):
        response = self.client.post(url_for('getfortune'), json={"year" : "2040", "luck" : "True"})
        print(response)
        self.assertIn(b'The double dice predicts a neutral fate', response.data)
    # Test neutral year and no double
    def test_fortune5(self):
        response = self.client.post(url_for('getfortune'), json={"year" : "2040", "luck" : "False"})
        print(response)
        self.assertIn(b'Your past, present and future are unknown', response.data)
    # Test double negative
    def test_fortune6(self):
        response = self.client.post(url_for('getfortune'), json={"year" : "2021", "luck" : "False"})
        print(response)
        self.assertIn(b'Bad things may be coming, avoid outside at all costs.', response.data)

