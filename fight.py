def fight_function(cells_in_focus):
    powerful_cells = []
    for cell in cells_in_focus:
        if powerful_cells:
            if cell.power > powerful_cells[0].power:
                powerful_cells = [cell]
            elif cell.power == powerful_cells[0].power:
                powerful_cells.append(cell)
        else:
            powerful_cells.append(cell)
    for cell in set(cells_in_focus) - set(powerful_cells):
        cell.is_alive = False
