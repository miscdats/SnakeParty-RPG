# number conversion mirror trick
# num_conversion.py

import arcade


class Mirror:

    def mirror_puzzle(self):
        pass

    @staticmethod
    def draw():
        """ Draws a mirror and returns it """
        trans_blue = arcade.make_transparent_color(arcade.color.AIR_SUPERIORITY_BLUE, 0.66)
        mirror = arcade.make_soft_circle_texture(5, trans_blue, 240, 10)

        return mirror

