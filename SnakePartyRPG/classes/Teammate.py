# friends of all types included here
import random
from spritesheets import *
import math


class Teammate(arcade.Sprite):
    bonus = None
    strength = 0
    name = None
    dialog = None
    mate_sprite = arcade.Sprite("images/pink_snake_tongue_pixel.png", WALL_SPRITE_SCALING)
    mate_sprite.center_x = random.randrange(SCREEN_WIDTH)
    mate_sprite.center_y = random.randrange(SCREEN_HEIGHT)

    def __init__(self, item_list):
        # Call the parent Sprite constructor
        super().__init__()
        if 25 > len(item_list) >= 5:
            self.name = "wracker"
            self.strength = 5
        elif 50 > len(item_list) >= 25:
            self.name = "pipo"
            self.strength = 25
        elif len(item_list) >= 50:
            self.name = "strompy"
            self.strength = 50
        self.mate_sprite.draw()

    def strompy_help(self, javelin_list):
        self.bonus = "destroy enemy weapons"
        self.strength = 50
        self.dialog = "Strompy's here to help!"

        for javelin in javelin_list:
            javelin.kill()

    def pipo_help(self, enemy_list):
        self.bonus = "destroy enemies"
        self.strength = 25
        self.dialog = "Pipo's here to help!"

        for enemy in enemy_list:
            enemy.kill()

    def wracker_help(self, mirror_list):
        self.bonus = "destroy mirrors"
        self.dialog = "Wracker's here to help!"

        for mirror in mirror_list:
            mirror.kill()

    def follow_sprite(self, player_sprite):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        if random.randrange(100) == 0:
            start_x = self.center_x
            start_y = self.center_y

            # Get the destination location for our mate
            dest_x = player_sprite.center_x
            dest_y = player_sprite.center_y

            # Do math to calculate how to get the teammate to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast our mate travels.
            self.change_x = math.cos(angle) * MOVEMENT_SPEED
            self.change_y = math.sin(angle) * MOVEMENT_SPEED

