from maineed.object import *

# 實體化
player = Player(psi)
pirate_ship = PirateShip()
boss = Boss(boss_psi)
screens = Screen()
# 加群
players.add(player)
pirate_ships.add(pirate_ship)
bosss.add(boss)

# 顯示順序
MAIN_SHOW.add(screens)
MAIN_SHOW.add(player)
for i in range(5):
    meteor = Meteor()
    MAIN_SHOW.add(meteor)
for i in range(20):
    rock = Rock()
    MAIN_SHOW.add(rock)
    rocks.add(rock)

MAIN_SHOW.add(pirate_ship)
MAIN_SHOW.add(boss)
