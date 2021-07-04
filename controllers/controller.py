from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/game')
def index():
    return render_template('index.html', title="RPS", players=players)

@app.route('/game', methods=['POST'])
def add_game():
    if player_one.request.form["choice"] == "Rock" 
    and player_two.request.form["choice"] == "Rock"
    return "Tie"



