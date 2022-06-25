from sys import stdout
from random import choice, sample
from colorama import Fore
from itertools import cycle


class Cell:
    color = Fore.WHITE
    power = None
    max_age = None

    def __init__(self, canvas, h=None, v=None):
        self._canvas = canvas
        self._h = h if h else canvas.random_h
        self._v = v if v else canvas.random_v
        self._body = cycle(sample([chr(186), chr(164)], 2))
        self.is_alive = True
        self._current_age = 0

    def is_in_position(self, h, v):
        return self._h == h and self._v == v

    def _random_walk_within_canvas(self):
        while True:
            new_h = self._h + choice([-1, 0, 1])
            if new_h > 0 and new_h < self._canvas.h_max - 1:
                break
        self._h = new_h

        while True:
            new_v = self._v + choice([-1, 0, 1])
            if new_v > 0 and new_v < self._canvas.v_max - 1:
                break
        self._v = new_v

    def _move(self):
        if not self.is_alive:
            return
        self._random_walk_within_canvas()

    def _age(self):
        if not self.is_alive:
            return
        self._current_age += 1
        if self.max_age and self._current_age > self.max_age:
            self.die()

    def die(self):
        self.is_alive = False

    def live(self):
        if not self.is_alive:
            return
        self._move()
        self._age()

    def draw(self):
        stdout.write(f"{self.color}{next(self._body)}{Fore.RESET}")


class RedCell(Cell):
    color = Fore.RED
    power = 20
    max_age = 100


class GreenCell(Cell):
    color = Fore.GREEN
    power = 15
    max_age = 200


class BlueCell(Cell):
    color = Fore.BLUE
    power = 10
    max_age = 400
