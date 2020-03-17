import random

# models for game pieces, players, ships, board(s)

#Player class
class PlayerClass:
    def __init__(self, name):
        self.name = name

# Battleship game class
class BattleshipClass:
    # define players array
    def __init__(self, players, activeplayer):
        self.players = players
        self.activeplayer = activeplayer
    
    def game_start(self):
        print("game is starting!")
    
    def game_end(self):
        print("game has ended!")

    def game_end_turn(self):
        print("turn has ended")

    def game_set_winner(self):
        print("winner is " + self.activeplayer.name)
        return

# tests

players = []

players.append(PlayerClass('jim'))
players.append(PlayerClass('John'))
players.append(PlayerClass('billy'))

activeplayer = random.randint(0, 2)
game = BattleshipClass(players, players[activeplayer])

for obj in game.players:
    print(obj.name)

print("\n" + game.activeplayer.name + 
" index " + str(activeplayer))

game.game_set_winner()