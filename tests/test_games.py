from urllib import response
from flask import url_for, redirect
     
from flask_testing import TestCase
from application import app, db
from application.models import Gamer,Game

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        bob = Gamer(name='Bob')
        ben = Gamer(name='Ben')
        joe = Gamer(name='Joe')
        game1 = Game(name='Argent The Consortium', gamerbr=bob)
        game2 = Game(name="Revolution", designer='Steve Jackson', gamerbr=bob)
        game3 = Game(name='Neanderthal', gamerbr=ben)
        db.session.add_all([bob,ben,game1,game2,game3])
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestDisplay(TestBase):
    def test_gamers(self):
        response = self.client.get(url_for('games'))
        self.assert200
        self.assertIn(b'Neanderthal', response.data)
