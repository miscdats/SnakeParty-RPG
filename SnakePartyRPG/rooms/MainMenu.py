# Draw a main menu and receive input
# for decisions made, continue game...

import arcade
from . import

# Constants for in-game menu
GAME_NAME = "SnakeParty RPG"

# Open window with title+dimensions+bg color; render
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_NAME)
arcade.set_background_color(arcade.color.ASH_GREY)
arcade.start_render()


class MainMenu:
    def MainMenu(self):


