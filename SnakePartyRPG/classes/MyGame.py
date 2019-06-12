import timeit

from room_builders.Treasury import *
from room_builders.VolcanoPit import *
from room_builders.ReflectingPools import *
from room_builders.CliffsArea import *
from room_builders.BattleRoom import *
from room_builders.Intro import *
from constants import *
import numpy as np
import arcade
import time
from classes.Party import *
from classes.Player import *
from classes.Turning import *
from classes.Teammate import *
from classes.Imp import *
from classes.Javelin import *
import itertools
from itertools import product
from itertools import permutations
from itertools import combinations
import string


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.current_room = 0

        # Set up the players
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.party_list = None
        self.item_list = None
        self.enemy_list = None
        self.javelin_list = None
        self.physics_engine = None
        self.score = 0
        self.mates = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite = arcade.Sprite("images/rogue.png", SPRITE_SCALING)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.item_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.javelin_list = arcade.SpriteList()
        self.party_list = set()

        # Score
        self.score = 0
        # Our list of rooms
        self.rooms = []

        # Create the room_builders.
        room = intro()
        self.rooms.append(room)

        room = cliffs_area()
        self.rooms.append(room)

        room = battle_room()
        self.rooms.append(room)

        room = reflecting_pools()
        self.rooms.append(room)

        room = volcano_pit()
        self.rooms.append(room)

        room = treasury()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """
        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.rooms[self.current_room].background)

        # Draw all the sprites in this room
        if self.current_room == 0:
            self.draw_instructions_page()
        else:
            self.player_sprite.draw()
            # self.player_list.draw()
            self.rooms[self.current_room].wall_list.draw()

            if self.current_room == 1:
                # Set up the items
                for i in range(2):
                    # Create the item instance
                    item = arcade.Sprite("images/16x16/Item__67.png", SPRITE_SCALING * 3)

                    # Position the item
                    item.center_x = random.randrange(SCREEN_WIDTH)
                    item.center_y = random.randrange(SCREEN_HEIGHT)

                    # Add the item to the lists
                    self.item_list.append(item)
                self.item_list.draw()

            if self.current_room == 2:
                # set up the enemy imp forces
                for i in range(1):
                    # Create the item instance
                    enemy = Imp("images/imp.png", SPRITE_SCALING)

                    # Position the item
                    enemy.center_x = random.randrange(SCREEN_WIDTH)
                    enemy.center_y = random.randrange(SCREEN_HEIGHT)

                    # Add the enemy to the lists
                    self.enemy_list.append(enemy)
                self.enemy_list.draw()
                # self.rooms[self.current_room].javelin_list.draw()

            if self.current_room == 5:
                # Put the text on the screen.
                output = "You made it!"
                arcade.draw_text(output, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.JUNE_BUD, 24)

            # # Draw inventory to screen...
            # arcade.draw_lrtb_rectangle_filled(350,
            #                                   350 + SCREEN_WIDTH - 1,
            #                                   700 + TEAM_SPRITE_SIZE * 2,
            #                                   700, arcade.color.BLACK)
            # x_position = 350

            # for item in self.item_list:
            #     item.bottom = -SCREEN_HEIGHT + 50
            #     item.left = x_position
            #     x_position += item.width
            #     item.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

            # Display timings
            output = f"Processing time: {self.processing_time:.3f}"
            arcade.draw_text(output, 20, SCREEN_HEIGHT - 20, arcade.color.WILD_ORCHID, 16)

            output = f"Drawing time: {self.draw_time:.3f}"
            arcade.draw_text(output, 20, SCREEN_HEIGHT - 40, arcade.color.WILD_WATERMELON, 16)

            if self.fps is not None:
                output = f"FPS: {self.fps:.0f}"
                arcade.draw_text(output, 20, SCREEN_HEIGHT - 60, arcade.color.WILLPOWER_ORANGE, 16)

            self.draw_time = timeit.default_timer() - draw_start_time

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        # intro state
        if self.current_room == 0:
            if key == arcade.key.SPACE:
                self.current_room = 1

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def draw_instructions_page(self):
        """ Draw and load instruction page as image. """
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        width = 800
        page_texture = arcade.load_texture("images/classic1.png")
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)
        arcade.draw_text("SnakeParty",
                         center_x + 2, center_y + 35, arcade.color.ALIZARIN_CRIMSON, 50, width=width, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("Party pals will give a bonus; but use them wisely or you'll have 1 in P chance to lose them!",
                         center_x - 50, center_y - 35, arcade.color.ANTI_FLASH_WHITE, 14, width=width, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("[WASD] to move, [SPACEBAR] to start, gather pies and don't dies!",
                         center_x, center_y - 85, arcade.color.ANTI_FLASH_WHITE, 14, width=width, align="center",
                         anchor_x="center", anchor_y="center")
        arcade.draw_text("Must have score over [00101] to succeed in this party.",
                         center_x, center_y - 125, arcade.color.ANTI_FLASH_WHITE, 14, width=width, align="center",
                         anchor_x="center", anchor_y="center")

    def game_of_chance(self):
        """ Creates probability of party member being killed off in pre-order fashion. """
        for i in range(1, self.mates + 1):
            turn = (np.random.randint(low=1, high=6))
            roll = turn
            if roll == self.mates:
                self.mates -= 1
                self.party_list.get_pre_order(self.player).kill()

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()

        if self.current_room == 1:
            # collect pies
            self.item_list.update()
            # Generate a list of all pie sprites that collided with the player.
            items_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.item_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for item in items_hit_list:
                item.kill()
                self.score += 1

        if self.current_room == 2:
            # avoid imps or lose pie points
            self.enemy_list.update()
            # Generate a list of all imp sprites that collided with the player.
            enemies_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
            # Loop through each colliding sprite, remove it, and deduct from the score.
            for imp in enemies_hit_list:
                imp.kill()
                self.score -= 1

        # got pie, get friends!
        if self.current_room == 3 and self.score >= 5:
            mate = Teammate(self.score)
            mate.follow_sprite(self.player_sprite)
            self.player_list.append(mate)
            mate.mate_sprite.draw()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 0:
            # intro room
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
            self.draw_instructions_page()

        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 1:
            # cliff area beginning room get items
            self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0

        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 2:
            # battle room combinations
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH
            # party_power = 0
            # team = list()
            # for mate in self.party_list.get_pre_order:
            #     party_power += Teammate.strength
            #     team.append(mate)
            # if party_power >= 25:
            #     for mate in list(combinations(team, 3)):
            #         if Teammate.name is "Pipo":
            #             Teammate.pipo_help(self.enemy_list)

        elif self.player_sprite.center_x < 0 and self.current_room == 3:
            # reflecting room conversion
            self.current_room = 4
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
            # friends fall to their lava deaths every so often [1:P chance]
            if self.mates > 0:
                start_time = time.time()
                while True:
                    self.game_of_chance()
                    time.sleep(60.0 - ((time.time() - start_time) % 60.0))

        elif self.player_sprite.center_x > SCREEN_WIDTH and self.current_room == 4\
                and self.score > 101:
            # volcanoes chance
            self.current_room = 5
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 150

        elif self.current_room == 5:
            # treasury

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 150
