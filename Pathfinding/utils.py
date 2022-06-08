import pygame


def h(point1: tuple, point2: tuple) -> int:
    '''
    Calculate the heuristic distance between two points.

    Args:
        * point1 (tuple) - The first point.
        * point2 (tuple) - The second point.

    Returns:
        * int - The heuristic distance.
    '''

    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def clickedGridPos(position: tuple, grid) -> tuple:
    '''
    Convert the pixel position to the position of the grid.

    Args:
        * grid (Grid) - The grid to calculate the position of.

    Returns:
        * tuple - The position of the node. (column, row)
    '''

    return (position[0] // (grid.node_size + grid.node_margin), position[1] // (grid.node_size + grid.node_margin))
