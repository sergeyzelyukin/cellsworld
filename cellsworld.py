#!/usr/bin/env python

import time

from cells import RedCell, BlueCell, GreenCell
from canvas import Canvas
from fight import fight_function


def main():
    canvas = Canvas(20, 10)
    canvas.add_cells(
        [
            RedCell(canvas=canvas),
            GreenCell(canvas=canvas),
            BlueCell(canvas=canvas),
        ]
    )
    canvas.on_cells_clash = fight_function

    for _ in range(100):
        canvas.draw_frame()
        time.sleep(1)
        canvas.poke_cells()


if __name__ == "__main__":
    main()
