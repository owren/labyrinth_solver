# Candidate no: 249

from values.Direction import Direction
from values.Path import Path


class Cell:
    """
    Class for keeping track of the status of each a given cell on the board
    Holds information about the walls and its coordinates and if it has been a part of the search
    """

    def __init__(self, y_coordinate, x_coordinate):
        # The walls is if there is a wall in given direction or not
        self.north_wall = False
        self.south_wall = False
        self.west_wall = False
        self.east_wall = False
        # The coordinates are the coordinates for given Cell object
        self.y_coordinate = y_coordinate
        self.x_coordinate = x_coordinate
        # If it is a part of the search
        self.path = Path.NO

    def update_wall(self, direction, wall):
        """
        Updates the wall for the Cell object in given direction, if there should be a wall there or not
        :param direction: Enum - Direction Enum, to decide what direction the wall should be updated, e.g. Direction.NORTH
        :param wall: boolean - True if there should be a wall, False if not wall
        """
        if direction == Direction.NORTH:
            self.north_wall = wall
        elif direction == Direction.SOUTH:
            self.south_wall = wall
        elif direction == Direction.WEST:
            self.west_wall = wall
        elif direction == Direction.EAST:
            self.east_wall = wall

    def get_wall(self, direction):
        """
        Getter for walls
        :param direction: Enum - Direction Enum, what wall we want to get from the Cell object
        :return: boolean - True if there is a wall, else False
        """
        if direction == Direction.NORTH:
            return self.north_wall
        elif direction == Direction.SOUTH:
            return self.south_wall
        elif direction == Direction.WEST:
            return self.west_wall
        elif direction == Direction.EAST:
            return self.east_wall

    def get_used(self):
        """
        Gets if the cell has been used or not 
        :return: Path Enum - NO, YES or WAS 
        """
        return self.path

    def set_used(self, path):
        """
        Sets if the cell has been used or not 
        :param path: Enum - NO, YES or WAS 
        """
        self.path = path
