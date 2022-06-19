#!/usr/bin/env python

import time

from cellsworld.cells import RedCell, BlueCell, GreenCell
from cellsworld.canvas import Canvas
from cellsworld.fight import fight_function

DEFAULT_FRAME_RATE = 0.2
DEFAULT_FRAMES_COUNT = 1000


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

    frames_count = DEFAULT_FRAMES_COUNT
    frame_rate = DEFAULT_FRAME_RATE
    for _ in range(frames_count):
        canvas.draw_frame()
        time.sleep(frame_rate)
        canvas.poke_cells()


if __name__ == "__main__":
    main()
