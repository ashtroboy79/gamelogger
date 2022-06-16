from application import db
from application.models import Gamer, Game

if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    bob = Gamer(name='Bob The Builder')
    joe = Gamer(name='Joe Blogs')
    ben = Gamer(name='Ben')
    game1 = Game(name='Argent The Consortium',rating=0, gamerbr=bob)
    game2 = Game(name="Revolution", designer='Steve Jackson',rating=0, gamerbr=bob)
    game3 = Game(name='Neanderthal', rating=0,gamerbr=ben)
    db.session.add_all([bob,joe,ben,game1,game2,game3])
    db.session.commit()
 
