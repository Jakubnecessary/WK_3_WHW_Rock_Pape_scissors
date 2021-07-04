from flask import render_template, request
from werkzeug.utils import redirect
from app import app
from models.player import *
from models.game import *

@app.route('/game')
def index():
    return render_template('index.html', title="RPS", players=players)



@app.route('/game', methods=['POST'])
def game():
    player_1.choice = request.form['player_1_choice']

    player_2.choice = request.form['player_2_choice']

        # player 1 rock
    if player_1.choice == "Rock" and player_2.choice == "Rock":
        return "Tie"
    elif player_1.choice == "Rock" and player_2.choice == "Scissors":
        return "Rock beats Scissors"
    elif player_1.choice == "Rock" and player_2.choice == "Paper":
        return "Paper Beats Rock"
    # player 1 paper
    elif player_1.choice == "Paper" and player_2.choice == "Rock":
        return "Paper Beats Rock"
    elif player_1.choice == "Paper" and player_2.choice == "Scissors":
        return "Scissors Beats Paper"
    elif player_1.choice == "Paper" and player_2.choice == "Paper":
        return "Tie"
    # player 1 scissors
    elif player_1.choice == "Scissors" and player_2.choice == "Rock":
        return "Rock Beats Scissors"
    elif player_1.choice == "Scissors" and player_2.choice == "Scissors":
        return "Tie"
    elif player_1.choice == "Scissors" and player_2.choice == "Paper":
        return "Scissors Beats Paper"
    add_new_game(game)
    return redirect('/game')
        
