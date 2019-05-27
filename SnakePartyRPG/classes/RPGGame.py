""" This is the main game / window class. """
import arcade
import random
import timeit
import os
import math

from constants import *
from algs import *
from rooms import *
from classes import *


class RPGGame(arcade.Window):
    """ Main application class. """

    def __init__(self, screen_width, screen_height, title):
        """ Constructor """
        super().__init__(screen_width, screen_height, title)

        # Set working directory
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Starts game state in first page of instructions
        self.current_state = INSTRUCTIONS_PAGE_0

        # No items or players yet
        self.item_list = None
        self.player_list = None
        self.room_list = None
        self.grid = None
        self.current_room = None

        self.view_bottom = 0
        self.view_left = 0
        self.physics_engine = None
        self.processing_time = 0
        self.draw_time = 0
        self.message_queue = None

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
        self.player_sprite = arcade.Sprite("images/character.png", TEAM_SPRITE_SIZE)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Set up the items
        for i in range(50):
            # Create the item instance
            item = arcade.Sprite("images/item_01.png", TEAM_SPRITE_SCALING / 3)

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
        center_x = SCREEN_WIDTH // 2 + self.view_left
        center_y = SCREEN_HEIGHT // 2 + self.view_bottom
        width = 400
        arcade.draw_text("Game Over",
                         center_x + 2, center_y - 35, arcade.color.ALIZARIN_CRIMSON, 50, width=width, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("Game Over",
                         center_x, center_y - 33, arcade.color.ANTI_FLASH_WHITE, 50, width=width, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("(Press 'R' to restart.)",
                         center_x, center_y - 85, arcade.color.ANTI_FLASH_WHITE, 14, width=width, align="center",
                         anchor_x="center", anchor_y="center")

    def draw_game(self):
        """ Draw all the sprites, along with the score. """
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # Draw all the sprites.
        self.player_list.draw()
        self.current_room.wall_list.draw()
        self.current_room.enemy_list.draw()
        self.current_room.item_list.draw()
        self.current_room.pewpew_list.draw()

        # Draw inventory
        arcade.draw_lrtb_rectangle_filled(self.view_left,
                                          self.view_left + SCREEN_WIDTH - 1,
                                          self.view_bottom + TEAM_SPRITE_SIZE * 2,
                                          self.view_bottom, arcade.color.BLACK)
        x_position = self.view_left

        for item in self.player_sprite.inventory:
            item.bottom = self.view_bottom
            item.left = x_position
            x_position += item.width
            item.draw()

            # Draw messages
            if len(self.message_queue) > 0:
                center_x = SCREEN_WIDTH // 2 + self.view_left
                center_y = SCREEN_HEIGHT // 2 + self.view_bottom
                width = 400
                arcade.draw_rectangle_filled(center_x, center_y,
                                             width, 200, arcade.color.BLACK)
                arcade.draw_rectangle_outline(center_x, center_y,
                                              width, 200, arcade.color.WHITE, 2)
                arcade.draw_text(self.message_queue[0],
                                 center_x, center_y + 10, arcade.color.WHITE, 14, width=width, align="center",
                                 anchor_x="center", anchor_y="center")

        self.draw_time = timeit.default_timer() - draw_start_time

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.AMERICAN_ROSE, 14)

    def on_draw(self):
        """ Render the screen according to current state. """
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def update(self, delta_time):
        """ All movement and game logic. """

        if not self.current_state == GAME_RUNNING:
            return

        if len(self.message_queue) > 0:
            return

        start_time = timeit.default_timer()

        # Move player
        self.physics_engine.update()

        # Move creatures
        for level in self.room_list:
            for enemy in level.enemy_list:
                enemy.update()

        for enemy in self.current_level.enemy_list:
            if enemy.tag == "goblin" and random.randrange(100) == 0:
                javelin = arcade.Sprite("images/javelin.png", 1)
                javelin.tag = "javelin"

                # Position the bullet at the player's current location
                start_x = enemy.center_x
                start_y = enemy.center_y
                javelin.center_x = start_x
                javelin.center_y = start_y

                # Get from mouse destination for impact
                dest_x = self.player_sprite.center_x
                dest_y = self.player_sprite.center_y

                # Trajectory for javelin throw
                x_diff = dest_x - start_x
                y_diff = dest_y - start_y
                angle = math.atan2(y_diff, x_diff)
                javelin.angle = math.degrees(angle)

                # velocity
                javelin.change_x = math.cos(angle) * JAVELIN_SPEED
                javelin.change_y = math.sin(angle) * JAVELIN_SPEED

                self.current_level.missile_list.append(javelin)

        # Generate a list of all item sprites that player picked up.
        objects_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.current_level.objects_list)
        for my_object in objects_hit_list:
            self.current_level.objects_list.remove(my_object)
            self.player_sprite.inventory.append(my_object)

        # Move javelins
        self.current_level.javelin_list.update()
        for javelin in self.current_level.javelin_list:
            sprites_hit = arcade.check_for_collision_with_list(javelin, self.current_level.wall_list)
            if len(sprites_hit) > 0:
                javelin.kill()

        # Did javelin hit player?
        sprites_hit = arcade.check_for_collision_with_list(self.player_sprite, self.current_room.javelin_list)
        if len(sprites_hit) > 25 || self.player.hp < 1:
            self.current_state = GAME_OVER

        nearest_sprite, distance = get_closest_sprite(self.player_sprite, self.current_level.enemy_list)

        if distance < TEAM_SPRITE_SIZE * 2 and nearest_sprite.tag == "cliff":
            self.message_queue.append("Oh look a cliff... HUH WAIT WHAT??? AHHHH!!!")
            self.current_state = GAME_OVER

        # --- Manage Scrolling ---
        self.scroll()

        # Save the time it took to do this.
        self.processing_time = timeit.default_timer() - start_time

    def on_key_press(self, key, modifiers):
        """ Called when a key is pressed. """

        # Instructions page
        if self.current_state == INSTRUCTIONS_PAGE_0:
            if key == arcade.key.SPACE:
                self.current_state = GAME_RUNNING
                arcade.set_background_color(self.current_level.background_color)

        # Game is running
        elif self.current_state == GAME_RUNNING:
            if key == arcade.key.SPACE and len(self.message_queue) > 0:
                self.message_queue.pop(0)
            elif len(self.message_queue) > 0:
                return
            elif key == arcade.key.SPACE:
                self.talk()
            elif key == arcade.key.W:
                self.player_sprite.change_y = MOVEMENT_SPEED
            elif key == arcade.key.S:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.A:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.D:
                self.player_sprite.change_x = MOVEMENT_SPEED

        # Game has ended
        elif self.current_state == GAME_OVER:
            if key == arcade.key.R:
                self.setup()
                self.current_state = INSTRUCTIONS_PAGE_0

    def on_key_release(self, key, modifiers):
        """ Called when user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def scroll(self):
        """ Track if we need to change the viewport. """

        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

def main():
    game = RPGGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()