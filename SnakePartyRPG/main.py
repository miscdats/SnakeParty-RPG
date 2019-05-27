import arcade

from constants import *
from classes import RPGGame


def main():
    game = RPGGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
