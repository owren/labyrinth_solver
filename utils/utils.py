# Candidate no: 249

import random

from values.Orientation import Orientation


def decide_orientation(width, height):
    """
    Decides the orientation for next recursive division
    If the height is bigger than the width - the split should be horizontal, vice versa for the opposite
    If the width and height are the same, then there is a random orientation
    Only being used by MazeGenerator.generator
    :param width: int - the width of the current division
    :param height: int - the height of the current division
    :return: enum - orientation of the split
    """
    if width < height:
        return Orientation.HORIZONTAL
    elif width > height:
        return Orientation.VERTICAL
    else:
        return Orientation.HORIZONTAL if random.randint(0, 1) == 0 else Orientation.VERTICAL
