# Whomever is playing assumes the role of player!
import arcade


class Player(arcade.Sprite):
    x = 10
    y = 10
    speed = 1

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)
        self.inventory = []

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed
