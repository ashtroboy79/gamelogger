# from tests import TestBase
from urllib import response
from flask import url_for, redirect
     
from flask_testing import TestCase
from application import app, db
from application.models import Gamer

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
        bob = Gamer(name='Bob The Builder')
        joe = Gamer(name='Joe Bloogs')
        db.session.add_all([bob,joe])
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestAdd(TestBase):
    def test_add_gamer(self):
        response = self.client.post(
            url_for('add_gamer'),
            data = dict(name='James Howlett')
            )
        assert list(Gamer.query.filter_by(name='James Howlett').all())[0].id == 3


class TestDisplay(TestBase):
    def test_gamers(self):
        response = self.client.get(url_for('gamers'))
        self.assert200
        self.assertIn(b'Bob The Builder', response.data)
