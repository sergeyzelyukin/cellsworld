from sys import stdout
from os import system
from random import randint
from colorama import Fore
from itertools import cycle


DOUBLE_VERTI_PIPE = "\u2551"
DOUBLE_HORIZ_PIPE = "\u2550"
DOUBLE_LEFT_TOP = "\u2554"
DOUBLE_LEFT_BOTTOM = "\u255a"
DOUBLE_RIGHT_TOP = "\u2557"
DOUBLE_RIGHT_BOTTOM = "\u255d"


class Canvas:
    def __init__(self, h_max, v_max):
        self.h_max = h_max
        self.v_max = v_max
        self.cells = []
        self.current_frame = 0
        self._progress_cycle = cycle(["-", "\\", "|", "/"])

    @property
    def random_h(self):
        return randint(1, self.h_max - 2)

    @property
    def random_v(self):
        return randint(1, self.v_max - 2)

    def add_cell(self, cell):
        self.cells.append(cell)

    def add_cells(self, cells):
        self.cells.extend(cells)

    def _get_position_background(self, h, v):
        background = " "
        if v == 0 or v == self.v_max - 1 or h == 0 or h == self.h_max - 1:
            if h == 0 or h == self.h_max - 1:
                background = DOUBLE_VERTI_PIPE
            elif v == 0 or v == self.v_max - 1:
                background = DOUBLE_HORIZ_PIPE
            if h == 0 and v == 0:
                background = DOUBLE_LEFT_TOP
            elif h == 0 and v == self.v_max - 1:
                background = DOUBLE_LEFT_BOTTOM
            elif h == self.h_max - 1 and v == 0:
                background = DOUBLE_RIGHT_TOP
            elif h == self.h_max - 1 and v == self.v_max - 1:
                background = DOUBLE_RIGHT_BOTTOM
        return background

    def _get_cells_in_focus(self, h, v):
        cells_in_focus = []
        for cell in self.cells:
            if cell.is_in_position(h, v):
                cells_in_focus.append(cell)
        return cells_in_focus

    def draw_frame(self):
        frame = ""
        for v in range(self.v_max):
            for h in range(self.h_max):
                background = self._get_position_background(h, v)

                cells_in_focus = self._get_cells_in_focus(h, v)
                if cells_in_focus:
                    if len(cells_in_focus) == 1:
                        frame += cells_in_focus[0].draw()
                    else:
                        self.on_cells_clash(cells_in_focus)
                        frame += f"{Fore.YELLOW}*{Fore.RESET}"
                else:
                    frame += background
            frame += "\n"
        self.current_frame += 1

        system("clear")
        stdout.write(frame)
        stdout.flush()

    def print_progress(self, frames_count):
        progress_pct = self.current_frame * 100 / frames_count
        done_bars = round(progress_pct * self.h_max / 100)
        rest_bars = self.h_max - done_bars
        stdout.write("*" * done_bars)
        if rest_bars > 0:
            stdout.write(next(self._progress_cycle) + "." * (rest_bars - 1))
        stdout.write("\n")
        stdout.flush()

    def animate_cells(self):
        for not_alive_cell in [cell for cell in self.cells if not cell.is_alive]:
            self.cells.remove(not_alive_cell)
        kids = []
        for cell in self.cells:
            kids.extend(cell.live())
        if kids:
            self.add_cells(kids)
