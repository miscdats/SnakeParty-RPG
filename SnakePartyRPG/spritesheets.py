import arcade
from constants import *



def read_sprite_list(grid, sprite_list):
    for row in grid:
        for grid_location in row:
            if grid_location.tile is not None:
                tile_sprite = arcade.Sprite(grid_location.tile.source, WALL_SPRITE_SCALING)
                tile_sprite.center_x = grid_location.center_x * WALL_SPRITE_SCALING
                tile_sprite.center_y = grid_location.center_y * WALL_SPRITE_SCALING
                # print(f"{grid_location.tile.source} -- ({tile_sprite.center_x:4}, {tile_sprite.center_y:4})")
                sprite_list.append(tile_sprite)

