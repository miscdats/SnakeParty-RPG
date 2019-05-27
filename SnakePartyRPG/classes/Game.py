import arcade
import random


# Game constants
SCREEN_TITLE = "SnakeParty RPG"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_SCALING = 0.5

# States the game can be in
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3


class Game(arcade.Window):
    """ Main application class. """

    def __init__(self, screen_width, screen_height, title):
        """ Constructor """
        super().__init__(screen_width, screen_height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Starts game state in first page of instructions
        self.current_state = INSTRUCTIONS_PAGE_0

        # No items or players yet
        self.item_list = None
        self.player_list = None

        # Set up player
        self.score = 0
        self.player_sprite = None

        # Instructions pages loaded
        self.instructions = []
        texture = arcade.load_texture("images/instructions_0.png")
        self.instructions.append(texture)
        texture = arcade.load_texture("images/instructions_1.png")
        self.instructions.append(texture)


    def setup(self):
        """ Game setup """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.item_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player_sprite = arcade.Sprite("images/character.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Set up the items
        for i in range(50):
            # Create the item instance
            item = arcade.Sprite("images/item_01.png", SPRITE_SCALING / 3)

            # Position the item
            item.center_x = random.randrange(SCREEN_WIDTH)
            item.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the item to the lists
            self.item_list.append(item)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def draw_instructions_page(self, page_number):
        """ Draw and load instruction page as image. """
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    @staticmethod
    def draw_game_over():
        """ Text "Game Over" drawn on screen. """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.ALIZARIN_CRIMSON, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.ANTI_FLASH_WHITE, 24)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        # Generate a list of all coin sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()