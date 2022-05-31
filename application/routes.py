from application import app, db
from application.models import Game, Gamer
from flask import redirect, render_template, url_for, request

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])

