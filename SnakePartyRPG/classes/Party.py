# made up of Player and teammates
# Player.py
# Teammate.py

# Bonuses in certain scenarios/rooms [party : strong / weak against...]
# permus_combinis.py

import numpy as np
from classes.Player import *


class Party:
    mates = 0
    party_list = None
    bonuses = None
    # schedule chat every 30s
    # arcade.schedule(the_talker, 30)

    def __init__(self):
        self.mates += 1
        self.party_list = []
        self.party_list.append(Player())

    def game_of_chance(self, num_rooms):
        """ Creates probability of party member being killed off. """
        for i in range(1, num_rooms + 1):
            turn = (np.random.randint(low=1, high=6))
            roll = turn
            if roll == self.mates:
                self.mates -= 1
                self.party_list[-1].kill()
