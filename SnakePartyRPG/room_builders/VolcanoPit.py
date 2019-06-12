
from constants import *
import arcade
from classes.Room import *


def volcano_pit():
    """
    Create and return Volcano Pit.
    """
    room = Room()

    room.name = "Volcano"
    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/nature_tileset_without_gaps/_lava/lava1.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            wall.tag = "firewall"
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("images/nature_tileset_without_gaps/_lava/lava1.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/nature_tileset_without_gaps/_lava/lava1.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 10 * SPRITE_SIZE
    room.wall_list.append(wall)

    # Load the background image for this level.
    room.background = arcade.load_texture("images/bgs/PNG/Full/Miscellaneous/volcanoes.png")

    return room
