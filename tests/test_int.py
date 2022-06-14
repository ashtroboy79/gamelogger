from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Gamer, Game

class TestBase(LiveServerTestCase):
    
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            DEBUG=True,
            LIVESERVER_PORT=5050,
            TESTING=True    
        )
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        db.create_all()
        bob = Gamer(name='Bob The Builder')
        joe = Gamer(name='Joe Blogs')
        ben = Gamer(name='Ben')
        game1 = Game(name='Argent The Consortium',rating=0, gamerbr=bob)
        game2 = Game(name="Revolution", designer='Steve Jackson',rating=0, gamerbr=bob)
        game3 = Game(name='Neanderthal', rating=0,gamerbr=ben)
        db.session.add_all([bob,joe,ben,game1,game2,game3])
        db.session.commit()
        
        self.driver.get(f'http://localhost:5050/')
        
    def tearDown(self):
        self.driver.quit()
        db.drop_all()
        
    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:5050/')
        self.assertEqual(response.code, 200)
        
        
        
        
# /html/body/div/p[1]/a

# /html/body/div/form[1]/button
