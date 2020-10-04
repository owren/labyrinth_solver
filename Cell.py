################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import random

from Types import *

class Cell:

    def __init__(self, y_coordinate, x_coordinate):
        self.north_wall = False
        self.south_wall = False
        self.west_wall = False
        self.east_wall = False
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate

    def update_wall(self, direction, wall):
        if direction == Direction.NORTH:
            self.north_wall = wall
        elif direction == Direction.SOUTH:
            self.south_wall = wall
        elif direction == Direction.WEST:
            self.west_wall = wall
        elif direction == Direction.EAST:
            self.east_wall = wall

    def get_wall(self, wall):
        if wall == Direction.NORTH:
            return self.north_wall
        elif wall == Direction.SOUTH:
            return self.south_wall
        elif wall == Direction.WEST:
            return self.west_wall
        elif wall == Direction.EAST:
            return self.east_wall
