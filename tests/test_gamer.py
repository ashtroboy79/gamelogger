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
        joe = Gamer(name='Joe Blogs')
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
    
    def test_add_game_get(self):
        response = self.client.get(url_for('add_gamer'))
        self.assert200(response)
        self.assertIn(b'Name', response.data)

class TestDisplay(TestBase):
    def test_gamers(self):
        response = self.client.get(url_for('gamers'))
        self.assert200(response)
        self.assertIn(b'Bob The Builder', response.data)


class TestUpdate(TestBase):
    def test_update_gamer_get(self):
        response = self.client.get(url_for('update_gamer', id=2))
        self.assert200(response)
        self.assertIn(b'Joe Blogs', response.data)
        
    def test_update_gamer(self):
        response = self.client.post(url_for('update_gamer', id=2),
                   data = dict(name="Scott Summers"),
                   follow_redirects=True
                    )
        self.assert200(response)
        self.assertIn(b'Scott Summers', response.data)
        
    
