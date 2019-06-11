# Room full of mirrored waters!
# Figure out how to escape...

from constants import *
import arcade
from classes.Room import *
from num_conversion import *


def reflecting_pools():
    """
    Create and return Reflecting Pools.
    """
    room = Room()

    room.name = "Reflecting"
    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of mirrors
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each mirror going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/nature_tileset_without_gaps/_water/water2_transp.png", WALL_SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            wall.tag = "mirror"
            wall.code = dec_to_bin(x)
            room.wall_list.append(wall)

    # Create left and right column of mirrors
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each mirror going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("images/nature_tileset_without_gaps/_water/water1_transp.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                wall.tag = "mirror"
                wall.code = dec_to_bin(x)
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/nature_tileset_without_gaps/_water/water_full_1.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 10 * SPRITE_SIZE
    room.wall_list.append(wall)
    room.background = arcade.load_texture("images/glacial/glacial_mountains_fullcolor_preview.png")

    return room
