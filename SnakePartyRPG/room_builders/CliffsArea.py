# On event of successful escape of Battle Rooms,
# you are chased out to the cliffs.
# Find out if you are capable of not drawing attention;
# else, can you survive?

# Then it is 3 firewalls, 1 cliff! Choose wisely.

from classes.Room import *


def cliffs_area():
    """
    Create and return Cliffs Area.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.item_list = arcade.SpriteList()

    # # collect pies
    # # Set up the items
    # for i in range(10):
    #     # Create the item instance
    #     item = arcade.Sprite("images/16x16/Item__67.png", SPRITE_SCALING * 3)
    #
    #     # Position the item
    #     item.center_x = random.randrange(SCREEN_WIDTH - 150)
    #     item.center_y = random.randrange(SCREEN_HEIGHT - 150)
    #
    #     # Add the item to the lists
    #     room.item_list.append(item)

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky04.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky04.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                wall.tag = "cliff"
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky04.png", SPRITE_SCALING)
    wall.left = 7 * SPRITE_SIZE
    wall.bottom = 5 * SPRITE_SIZE
    room.wall_list.append(wall)

    room.problem = "Find the will to live!"

    if room.is_answered is True:
        room.key = arcade.Sprite("images/16x16/Item__69.png", WALL_SPRITE_SCALING)
        room.key.center_x = random.randrange(SCREEN_WIDTH)
        room.key.center_y = random.randrange(SCREEN_HEIGHT)
        room.key.draw()

    # Load the background image for this level.
    room.background = arcade.load_texture("images/bgs/PNG/Full/Horror/horror2_nomoon.png")

    return room
