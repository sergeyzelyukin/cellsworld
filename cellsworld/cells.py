from sys import stdout
from random import choice, sample, seed
from colorama import Fore
from itertools import cycle


def alive_only(func):
    def inner_func(obj, *args, **kwargs):
        if not obj.is_alive:
            return
        return func(obj, *args, **kwargs)

    return inner_func


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
        self._clashed = False

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

    @alive_only
    def _move(self):
        self._clashed = False
        self._random_walk_within_canvas()

    @alive_only
    def _age(self):
        self._current_age += 1
        if self.max_age and self._current_age > self.max_age:
            self.die()

    def die(self):
        self.is_alive = False

    @alive_only
    def _reproduce(self):
        if self._clashed:
            return []
        if (
            not self._current_age == 0
            and self._current_age % self.reproduction_period == 0
        ):
            return [
                self.__class__(canvas=self._canvas, h=self._h, v=self._v)
                for _ in range(self.number_of_kids)
            ]
        return []

    @alive_only
    def live(self):
        kids = self._reproduce()
        self._move()
        self._age()
        return kids

    def clash(self):
        self._clashed = True

    def draw(self):
        stdout.write(f"{self.color}{next(self._body)}{Fore.RESET}")


class RedCell(Cell):
    color = Fore.RED
    power = 20
    max_age = 50
    reproduction_period = 40
    number_of_kids = 1


class GreenCell(Cell):
    color = Fore.GREEN
    power = 15
    max_age = 30
    reproduction_period = 20
    number_of_kids = 1


class BlueCell(Cell):
    color = Fore.BLUE
    power = 10
    max_age = 5
    reproduction_period = 3
    number_of_kids = 1
