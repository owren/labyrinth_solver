# Candidate no: 249

from enum import Enum


class Path(Enum):
    """
    Path enum; no, yeas, was
    Used to check if a cell is or has been in the search
    """
    NO = 0
    YES = 1
    WAS = 2
