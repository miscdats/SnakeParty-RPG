import random
import arcade
from constants import *


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # Lists for coins, monsters, etc.
        self.name = None
        self.party_list = None
        self.wall_list = None
        self.enemy_list = None
        self.javelin_list = None
        self.item_list = None
        self.coin_list = None
        self.background = None
        self.problem = None
        self.score = None
        self.is_answered = False
        self.key = arcade.Sprite("images/16x16/Item__69.png", WALL_SPRITE_SCALING)
        self.key.center_x = random.randrange(SCREEN_WIDTH)
        self.key.center_y = random.randrange(SCREEN_HEIGHT)
