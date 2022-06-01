from crypt import methods
from application import app, db
from application.models import Game, Gamer
from flask import redirect, render_template, url_for, request
from application.forms import gamerForm, gameForm

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/gamers')
def gamers():
    gamer = Gamer.query.all()
    return render_template('gamer.html', gamers=gamer)

@app.route('/gamers/add', methods=['GET', 'POST'])
def add_gamer():
    form = gamerForm()
    if form.validate_on_submit():
        name = form.name.data
        gamer = Gamer(name=name)
        db.session.add(gamer)
        db.session.commit()
        return redirect(url_for('gamers'))
    return render_template('user_add.html', form=form)

@app.route('/games')
def games():
    games = Game.query.all()
    return render_template('games.html', games=games)

@app.route('/games/add', methods=['GET', 'POST'])
def add_game():
    form = gameForm()
    gamers = Gamer.query.all()
    for gamer in gamers:
        form.gamer_id.choices.append((gamer.id,f"{gamer.name}"))
    if form.validate_on_submit():
        game = form.name.data
        designer = form.designer.data
        genre = form.genre.data
        rating = form.rating.data
        gamer_id = form.gamer_id.data
        new_game = Game(name=game, designer=designer, genre=genre, rating=rating, gamer_id=gamer_id)
        db.session.add(new_game)
        db.session.commit()
        return redirect(url_for('games'))
    return render_template('game_add.html', form=form)
