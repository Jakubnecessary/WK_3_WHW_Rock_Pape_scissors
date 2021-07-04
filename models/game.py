from models.player import *


player_1 = Player("Jack", "Rock")
player_2 = Player("Mike", "Scissors")
player_3 = Player("Jan", "Paper")

players = [player_1, player_2, player_3]

game_1 = [player_1.choice, player_2.choice]
games = [game_1]


def add_new_player(player):
    players.append(player)

def add_new_game(game):
    games.append(game)


def game_logic():
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
