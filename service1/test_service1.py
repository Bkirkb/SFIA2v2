from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

import requests_mock
from application import app,db
from application.models import Fortune2

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Fortune2(yearmon="23 January", fortune="Test fortune", luck="False"))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

  def test_page(self):
    with requests_mock.mock() as a:
        a.get('http://fortune-swarm_service2:5000/getyearmon', json={"year" : "2023", "month" : "January"} )
        a.get('http://fortune-swarm_service3:5000/getluck', text="False")
        a.post('http://fortune-swarm_service4:5000/getfortune', text="Your luck is not with the dice rolls, but your future is bright")

        response = self.client.get(url_for('index'))

        self.assertIn(b'January 2023', response.data)
        self.assertIn(b'Your luck is not with the dice rolls, but your future is bright', response.data)