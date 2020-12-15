################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from enum import Enum


class Direction(Enum):
    """
    Enum for direction; north, south, east, west
    Used for checking and setting walls for cells
    """
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3
