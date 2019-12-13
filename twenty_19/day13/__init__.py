from twenty_19.day8 import print_image
from twenty_19.util.devices import FrameBuffer


class GamePlayerDevice(FrameBuffer):
    class Sprite:
        def __init__(self, repr):
            self.repr = repr

    def __init__(self, width, height):
        super().__init__(width * height)
        self.width = width
        self.height = height
        self.clear()
        self.blocks = set()
        self.first_render_complete = False
        self.previous_ball_pos = None
        self.previous_paddle_pos = None

        self.sprites = {
            0: self.Sprite([0]),
            1: self.Sprite([1]),
            2: self.Sprite([1]),
            3: self.Sprite([1, 1]),
            4: self.Sprite([2])
        }

    def read(self):
        """
        Automate the playing of the game.
        The ball can only move in the x direction one position at a time, so move the paddle with it and it will
        never miss.
        """
        if self.previous_paddle_pos[0] < self.previous_ball_pos[0]:
            return 1
        if self.previous_paddle_pos[0] > self.previous_ball_pos[0]:
            return -1
        return 0

    def write(self, value):
        if self.x == None:
            self.x = value
        elif self.y == None:
            self.y = value
        elif self.x == -1 and self.y == 0:
            self.score = value
            self.clear()
            print("Score: ", self.score)
        else:
            # record the block
            position = (self.x, self.y)
            if value == 2:
                self.blocks.add(position)

            if value == 3:
                if self.previous_paddle_pos:
                    # write an empty paddle into memory to clear the ball from the frame buffer
                    super().write((self.previous_paddle_pos[1] * self.width) + self.previous_paddle_pos[0], [0, 0])
                self.previous_paddle_pos = position

            # if it's a ball, clear the framebuffer of the previous ball position
            if value == 4:
                if self.previous_ball_pos:
                    # write an empty block into memory to clear the ball from the frame buffer
                    super().write((self.previous_ball_pos[1] * self.width) + self.previous_ball_pos[0], self.sprites[0].repr)

                self.previous_ball_pos = position

                if position in self.blocks:
                    self.blocks.remove(position)
                    # write an empty block into memory to clear it from the frame buffer
                    super().write((self.y * self.width) + self.x, self.sprites[0].repr)
                    if len(self.blocks) == 0:
                        print("Final Score: ", self.score)

            super().write((self.y * self.width) + self.x, self.sprites[value].repr)

            if (self.x == self.width and self.y == self.height) or self.first_render_complete:
                self.first_render_complete = True
                print_image(super().dump_memory(), self.width, self.height)

            self.clear()

    def clear(self):
        self.y = None
        self.x = None