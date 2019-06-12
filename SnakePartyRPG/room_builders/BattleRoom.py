# If you end up in the wrong room, you may encounter enemies!
# Battle the foes and fiends until successfully outmaneuvering them
# or defeating them! Be careful not to overestimate yourself...

# Probability?
# probabilities.py

# Battle goes on while hp > 0
# Run away option available if stamina > 30

from classes.Room import *


def battle_room():
    """
    Create and return Battle Room!!!
    """
    room = Room()
    room.name = "Battle"
    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()
    room.enemy_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky02.png", SPRITE_SCALING)
            wall.left = x
            wall.bottom = y
            wall.tag = "spike"
            room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - WALL_SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 3 and 5 blocks up on the right side
            if (y != SPRITE_SIZE * 3 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky03.png", SPRITE_SCALING)
                wall.left = y
                wall.bottom = x
                wall.tag = "spike"
                room.wall_list.append(wall)

    wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky03.png", SPRITE_SCALING)
    wall.left = 3 * SPRITE_SIZE
    wall.bottom = 2 * SPRITE_SIZE
    room.wall_list.append(wall)
    wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky03.png", SPRITE_SCALING)
    wall.left = 9 * SPRITE_SIZE
    wall.bottom = 9 * SPRITE_SIZE
    room.wall_list.append(wall)
    wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky03.png", SPRITE_SCALING)
    wall.left = 5 * SPRITE_SIZE
    wall.bottom = 4 * SPRITE_SIZE
    room.wall_list.append(wall)
    wall = arcade.Sprite("images/nature_tileset_without_gaps/_rocky/rocky03.png", SPRITE_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)

    room.problem = "Attack with [spacebar]!"

    if room.is_answered is True:
        room.key.draw()

    # Load the background image for this level.
    room.background = arcade.load_texture("images/bgs/PNG/Full/Horror/horror1.png")

    return room

