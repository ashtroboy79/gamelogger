from application import db
from application.models import Gamer, Game

db.drop_all()
db.create_all()

bob = Gamer(name='Bob')
ben = Gamer(name='Ben')
joe = Gamer(name='Joe')

game1 = Game(name='Argent The Consortium', gamerbr=bob)
game2 = Game(name="Revolution", designer='Steve Jackson', gamerbr=bob)
game3 = Game(name='Neanderthal', gamerbr=ben)

db.session.add_all([bob,ben,game1,game2,game3])
db.session.commit()
