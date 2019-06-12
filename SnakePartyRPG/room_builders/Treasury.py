# Room full of it!
# get rich quick schemes

from classes.Room import *
from num_conversion import *


def treasury():
    """
    Create and return Treasury.
    """
    room = Room()

    room.name = "Treasury"
    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.item_list = arcade.SpriteList()

    # collect pies
    # Set up the items
    for i in range(10):
        # Create the item instance
        item = arcade.Sprite("images/16x16/Item__67.png", SPRITE_SCALING)

        # Position the item
        item.center_x = random.randrange(SCREEN_WIDTH - 150)
        item.center_y = random.randrange(SCREEN_HEIGHT - 150)

        # Add the item to the lists
        room.item_list.append(item)

    # -- Set up the walls
    # Create bottom and top row of mirrors
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each mirror going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/16x16/Item__71.png", SPRITE_SCALING*5)
            wall.left = x
            wall.bottom = y
            wall.tag = "trophy"
            room.wall_list.append(wall)

    # Create left and right column of mirrors
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each mirror going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("images/16x16/Item__71.png", SPRITE_SCALING*5)
                wall.left = x
                wall.bottom = y
                wall.tag = "trophy"
                room.wall_list.append(wall)

    spirals = []
    spirals = fibonacci(500)

    for i in spirals:
        for j in spirals:
            wall = arcade.Sprite("images/16x16/Item__71.png", SPRITE_SCALING*3)
            wall.left = j * SPRITE_SCALING + 300
            wall.bottom = i * SPRITE_SCALING + 200
            room.wall_list.append(wall)

    room.background = arcade.load_texture("images/bgs/PNG/Full/City/classic_city.png")

    return room


def fibonacci(n):
    """ Returns array of numbers in Fibonacci sequence up to n. """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
