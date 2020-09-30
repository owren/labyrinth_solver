################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import random
import os
import time

from Types import Orientation

VER, HOR = 0, 1

def decide_orientation(width, height):
    if width < height:
        return Orientation.HORIZONTAL
    elif width > height:
        return Orientation.VERTICAL
    else:
        return Orientation.HORIZONTAL if random.randint(0, 1) == 0 else Orientation.VERTICAL


def clear_screen():
    """
    Clears the terminal screen for the game to be prettier
    """
    #wait(.01)
    os.system('cls' if os.name == 'nt' else 'clear')


def wait(x):
    time.sleep(x)


def random_even_number(min, max):
    while True:
        line = random.randint(min + 1, max - 1)
        if line % 2 == 0:
            return line
        else:
            continue


def random_odd_number(min, max):
    while True:
        line = random.randint(min, max)
        if line % 2 == 0:
            continue
        else:
            return line
