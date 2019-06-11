from classes import Turning


class Javelin(Turning):
    """
    Class that represents a javelin.

    Derives from arcade.TurningSprite which is just a Sprite
    that aligns to its direction.
    """

    sprite.tag = "javelin"

    def update(self):
        super().update()
        if self.center_x < -100 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
            self.kill()
