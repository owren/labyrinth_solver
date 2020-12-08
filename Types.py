from enum import Enum


class Orientation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1


class Direction(Enum):
    NORTH = 0
    SOUTH = 1
    WEST = 2
    EAST = 3


class Path(Enum):
    NO = 0
    YES = 1
    WAS = 2
