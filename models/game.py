from models.player import *


player_1 = Player("Jack", "Rock")
player_2 = Player("Mike", "Scissors")
player_3 = Player("Jan", "Paper")

players = [player_1, player_2, player_3]

def add_new_game(player):
    players.append(player)
