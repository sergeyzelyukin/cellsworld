from sys import stdout
from random import choice, sample
from colorama import Fore
from itertools import cycle


class Cell:
    def __init__(self, color, power, canvas, h=None, v=None):
        self._body = cycle(sample([chr(186), chr(164)], 2))
        self._color = color
        self.power = power
        self._canvas = canvas
        self.h = h if h else canvas.random_h
        self.v = v if v else canvas.random_v
        self.is_alive = True

    def _random_walk_within_canvas(self):
        while True:
            new_h = self.h + choice([-1, 0, 1])
            if new_h > 0 and new_h < self._canvas.h_max - 1:
                break
        self.h = new_h

        while True:
            new_v = self.v + choice([-1, 0, 1])
            if new_v > 0 and new_v < self._canvas.v_max - 1:
                break
        self.v = new_v

    def move(self):
        self._random_walk_within_canvas()

    def draw(self):
        stdout.write(f"{self._color}{next(self._body)}{Fore.RESET}")


class RedCell(Cell):
    power = 20

    def __init__(self, canvas, h=None, v=None):
        super().__init__(color=Fore.RED, power=self.power, canvas=canvas, h=h, v=v)


class GreenCell(Cell):
    power = 15

    def __init__(self, canvas, h=None, v=None):
        super().__init__(color=Fore.GREEN, power=self.power, canvas=canvas, h=h, v=v)


class BlueCell(Cell):
    power = 10

    def __init__(self, canvas, h=None, v=None):
        super().__init__(color=Fore.BLUE, power=self.power, canvas=canvas, h=h, v=v)
