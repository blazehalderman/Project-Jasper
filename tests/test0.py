from battleship_ai.models import (random, PlayerClass, BattleshipGameClass)

#populating players in battleship class

players = []

players.append(PlayerClass('jim'))
players.append(PlayerClass('John'))
players.append(PlayerClass('billy'))

activeplayer = random.randint(0, 2)
game = BattleshipGameClass(players, players[activeplayer])

for obj in game.players:
    print(obj.name)

print("\n" + game.activeplayer.name + 
" index " + str(activeplayer))

game.game_set_winner()