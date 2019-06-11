# On event of successful escape of Battle Rooms,
# you are chased out to the cliffs.
# Find out if you are capable of not drawing attention;
# else, can you survive?

# Then it is 3 firewalls, 1 cliff! Choose wisely.

from classes.Room import *


def intro():
    """
    Create and return instructions area.
    """
    room = Room()
    room.name = "Intro"
    """ Set up the game and initialize the variables. """

    if room.is_answered is True:
        room.key = arcade.Sprite("images/16x16/Item__69.png", WALL_SPRITE_SCALING)
        room.key.center_x = random.randrange(SCREEN_WIDTH)
        room.key.center_y = random.randrange(SCREEN_HEIGHT)
        room.key.draw()

    # Load the background image for this level.
    room.background = arcade.load_texture("images/classic1.png")

    room.wall_list = arcade.SpriteList()

    return room

