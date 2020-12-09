################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from robust_IO import input_int
from Constants import *
import visualization

import pygame


def main():
    #rows = int(input('Vertical size: '))
    #columns = int(input('Horizontal size: '))
    #y_coordinate = int(input('Y-coordinate for starting point: '))
    #x_coordinate = int(input('X-coordinate for starting point: '))
    x_coordinate = y_coordinate = 0
    rows = 60
    columns = 120
    visualization.start_pygame(rows, columns, x_coordinate, y_coordinate)


if __name__ == "__main__":
    main()
