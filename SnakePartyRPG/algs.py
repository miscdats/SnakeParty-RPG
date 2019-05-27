# Helpful algorithms.
import random
import arcade
import math
from constants import *


def randomly_place_sprite(sprite, wall_list):
    """ Place player randomly. If we are in a wall, repeat until we aren't. """
    placed = False
    while not placed:

        # Randomly position
        sprite.center_x = random.randrange(AREA_WIDTH)
        sprite.center_y = random.randrange(AREA_HEIGHT)

        # Are we in a wall?
        walls_hit = arcade.check_for_collision_with_list(sprite, wall_list)
        if len(walls_hit) == 0:
            # Not in a wall! Success!
            placed = True


def get_distance_between_sprites(sprite1, sprite2):
    distance = math.sqrt((sprite1.center_x - sprite2.center_x) ** 2 + (sprite1.center_y - sprite2.center_y) ** 2)
    return distance


def get_closest_sprite(sprite1, sprite_list) -> (arcade.Sprite, float):
    if len(sprite_list) == 0:
        return None

    min_pos = 0
    min_distance = get_distance_between_sprites(sprite1, sprite_list[min_pos])
    for i in range(1, len(sprite_list)):
        distance = get_distance_between_sprites(sprite1, sprite_list[i])
        if distance < min_distance:
            min_pos = i
            min_distance = distance
    return sprite_list[min_pos], min_distance
