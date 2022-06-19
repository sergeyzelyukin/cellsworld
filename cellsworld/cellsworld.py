#!/usr/bin/env python

import time
import click

from cellsworld.cells import RedCell, BlueCell, GreenCell
from cellsworld.canvas import Canvas
from cellsworld.fight import fight_function

DEFAULT_FRAME_RATE = 0.2
DEFAULT_FRAMES_COUNT = 1000
DEFAULT_WIDTH = 20
DEFAULT_HEIGHT = 10


@click.command()
@click.argument("width", type=int, default=DEFAULT_WIDTH)
@click.argument("height", type=int, default=DEFAULT_HEIGHT)
@click.argument("frames_count", type=int, default=DEFAULT_FRAMES_COUNT)
@click.argument("frame_rate", type=float, default=DEFAULT_FRAME_RATE)
def start(width, height, frames_count, frame_rate):
    canvas = Canvas(width, height)
    canvas.add_cells(
        [
            RedCell(canvas=canvas),
            GreenCell(canvas=canvas),
            BlueCell(canvas=canvas),
        ]
    )
    canvas.on_cells_clash = fight_function

    for _ in range(frames_count):
        canvas.draw_frame()
        time.sleep(frame_rate)
        canvas.poke_cells()


if __name__ == "__main__":
    start()
