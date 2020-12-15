# Candidate no: 249

from enum import Enum


class Orientation(Enum):
    """
    Orientation enum; vertical or horizontal
    Used for setting orientation of new splits in recursive divider
    """
    VERTICAL = 0
    HORIZONTAL = 1
