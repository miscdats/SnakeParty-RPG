# Each area is a room made of walls of fire!
# Who did this!?!?!?!?
# Oh well, try hard to get through!

# cipher puzzle
# prime_num_cipher.py

from pygame.locals import *
import pygame
import time


class FireWall:
    x = 0
    y = 0
    step = 44

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))



