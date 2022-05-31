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
