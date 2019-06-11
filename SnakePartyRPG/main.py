# where to start
from pyglet.gl import *

from classes.RPGGame import *

window = pyglet.window.Window()

# Set working directory
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


def main():
    game = RPGGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
