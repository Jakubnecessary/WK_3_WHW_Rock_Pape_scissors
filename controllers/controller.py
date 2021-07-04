from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/game')
def index():
    return render_template('index.html', title="RPS", players=players)




