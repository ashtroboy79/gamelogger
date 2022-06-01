from application import db
from application.models import Gamer, Game

db.drop_all()
db.create_all()

db.create_all()
bob = Gamer(name='Bob')
ben = Gamer(name='Ben')
joe = Gamer(name='Joe')
game1 = Game(name='Argent The Consortium',rating=0, gamerbr=bob)
game2 = Game(name="Revolution", designer='Steve Jackson',rating=0, gamerbr=bob)
game3 = Game(name='Neanderthal', rating=0,gamerbr=ben)
db.session.add_all([bob,ben,joe,game1,game2,game3])
db.session.commit()
