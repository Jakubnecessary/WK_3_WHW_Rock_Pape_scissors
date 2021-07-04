from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/game')
def index():
    return render_template('index.html', title="Home", players=players)

# @app.route('/game', methods=['post'])
# def add_game():
#     name = request.form['name']
#     choice = request.form['choice']
#     if request.form['choice'] == "Rock":
