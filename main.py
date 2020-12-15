################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from maze.Board import Board
from utils.robust_IO import input_int
from values import Constants
import visualization
from MazeSolver import MazeSolver
from UserInterface import UserInterface

import pygame


def main():
    """
    rows = input_int('Vertical size: ', 2, int(Constants.V_SIZE / 2))
    columns = input_int('Horizontal size: ', 2, rows * 2)
    y_coordinate = input_int('Y-coordinate starting point: ', 0, rows - 1)
    x_coordinate = input_int('X-coordinate starting point: ', 0, columns - 1)

    rows = 50
    columns = 100
    x_coordinate = int(columns / 2)
    y_coordinate = int(rows / 2)
    """
    ui = UserInterface()
    ui.run_loop()



if __name__ == "__main__":
    main()
