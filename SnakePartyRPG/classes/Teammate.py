# friends of all types included here
import random
from spritesheets import *


class Teammate(arcade.Sprite):
    bonus = None
    dialog = None
    sprite_model = read_sprite_list(50, "images/snake_spritesheet_calciumtrice.png")
    mate_sprite = arcade.Sprite(sprite_model, WALL_SPRITE_SCALING)
    mate_sprite.center_x = random.randrange(SCREEN_WIDTH)
    mate_sprite.center_y = random.randrange(SCREEN_HEIGHT)

    def __init__(self):
        # Call the parent Sprite constructor
        super().__init__()
        self.mate_sprite.draw()

    def strompy_help(self, javelin_list):
        self.bonus = "destroy enemy weapons"
        self.dialog = "Strompy's here to help!"

        for javelin in javelin_list:
            javelin.kill()

    def pipo_help(self, enemy_list):
        self.bonus = "destroy enemies"
        self.dialog = "Pipo's here to help!"

        for enemy in enemy_list:
            enemy.kill()
