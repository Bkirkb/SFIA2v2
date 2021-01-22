from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

import requests_mock
from application import app,db
from application.models import Fortune

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Fortune(day="23 January", fortune="You are a lucky individual, the gods have favoured your path and await good results"))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

  def test_page(self):
    with requests_mock.mock() as a:
        a.get('http://fortune-swarm_service2:5000/getday', json={"day" : "7", "month" : "January"})
        a.get('http://fortune-swarm_service3:5000/getluck', text="79")
        a.post('http://fortune-swarm_service4:5000/getfortune', text="You are a lucky individual, the gods have favoured your path and await good results")

        response = self.client.get(url_for('index'))

        self.assertIn(b'7 January', response.data)
        self.assertIn(b'You are a lucky individual, the gods have favoured your path and await good results', response.data)