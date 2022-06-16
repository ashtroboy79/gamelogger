from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import Gamer, Game
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


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
        self.driver.maximize_window()
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
        
               
class GamerTests(TestBase):
    def test_display_gamers(self):
       
        element = self.driver.find_element_by_xpath('/html/body/p[1]/a')
        element.click()
        
        assert self.driver.current_url == 'http://localhost:5050/gamers'
        self.assertIn("Bob The Builder", self.driver.page_source)
        
    def test_display_gamer(self):
        
        element = self.driver.find_element_by_xpath('/html/body/p[1]/a')
        element.click()
        
        element = self.driver.find_element_by_xpath('/html/body/div/p[1]/a')
        element.click()
        
        assert self.driver.current_url == 'http://localhost:5050/gamers/1'
        self.assertIn("Bob The Builder's Games", self.driver.page_source)

        
    def test_update_gamer(self):
        
        self.driver.find_element_by_xpath('/html/body/p[1]/a').click() # go from homepage to gamers page
        assert self.driver.current_url == 'http://localhost:5050/gamers' # check we are on the correct page
        
        self.driver.find_element_by_xpath('/html/body/div/p[2]/a').click() # go from gamers page to gamer update page
        assert self.driver.current_url == 'http://localhost:5050/gamers/update/1' # chack we are on the right page
        
        element = self.driver.find_element(By.NAME, "name") # find name input field
        element.send_keys("Batman")

        assert self.driver.current_url == 'http://localhost:5050/gamers/update/1'
        self.driver.find_element(By.NAME, "submit").click() # click submit
        
        assert self.driver.current_url == 'http://localhost:5050/gamers' 
        self.assertIn("Batman See my games", self.driver.page_source)
        
        
class GameTests(TestBase):
        
    def test_display_games(self):
        
        element = self.driver.find_element_by_xpath('/html/body/p[2]/a')
        element.click()
        
        assert self.driver.current_url == 'http://localhost:5050/games'
        self.assertIn("Revolution", self.driver.page_source)
        
