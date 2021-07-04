from models.player import *


player_1 = Player("Jack", "Rock")
player_2 = Player("Mike", "Scissors")
player_3 = Player("Jan", "Paper")

players = [player_1, player_2, player_3]

def add_new_player(player):
    players.append(player)

def game_logic():
    if player_1.choice == "Rock" and player_2.choice == "Rock":
        return "Tie"
    elif player_1.choice == "Rock" and player_2.choice == "Scissors":
        return "Rock beats Scissors"
    elif player_1.choice
