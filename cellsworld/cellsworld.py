#!/usr/bin/env python

import time
import click

from cellsworld.cells import RedCell, BlueCell, GreenCell
from cellsworld.canvas import Canvas
from cellsworld.fight import fight_function

DEFAULT_FRAME_RATE = 0.2
DEFAULT_FRAMES_COUNT = 200
DEFAULT_WIDTH = 40
DEFAULT_HEIGHT = 20


@click.command()
@click.option("--width", type=int, default=DEFAULT_WIDTH)
@click.option("--height", type=int, default=DEFAULT_HEIGHT)
@click.option("--frames_count", type=int, default=DEFAULT_FRAMES_COUNT)
@click.option("--frame_rate", type=float, default=DEFAULT_FRAME_RATE)
def start(width, height, frames_count, frame_rate):
    canvas = Canvas(width, height)
    canvas.add_cells(
        [
            RedCell(canvas=canvas),
            RedCell(canvas=canvas),
            RedCell(canvas=canvas),
            GreenCell(canvas=canvas),
            GreenCell(canvas=canvas),
            GreenCell(canvas=canvas),
            BlueCell(canvas=canvas),
            BlueCell(canvas=canvas),
            BlueCell(canvas=canvas),
        ]
    )
    canvas.on_cells_clash = fight_function

    for _ in range(frames_count):
        canvas.draw_frame()
        canvas.print_progress(frames_count)
        time.sleep(frame_rate)
        canvas.animate_cells()


if __name__ == "__main__":
    start()
