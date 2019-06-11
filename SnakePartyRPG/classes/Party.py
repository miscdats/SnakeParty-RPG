# made up of Player and teammates
# Player.py
# Teammate.py

# Bonuses in certain scenarios/rooms [party : strong / weak against...]
# permus_combinis.py

from classes.Player import *
from bs_trees import *


class Party:
    mates = 0
    party_list = None
    bonuses = None
    strength = 0
    player = None
    # schedule chat every 30s
    # arcade.schedule(the_talker, 30)

    def __init__(self):
        self.player = Player()
        self.party_list = BSTree()
        self.mates += 1
        self.party_list.insert(self.player)

