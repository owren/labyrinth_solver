################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import random
import os


def decide_orientation(width, height):
    if width > height:
        return 0
    elif width < height:
        return 1
    else:
        return 1 if random.randint(0, 1) == 0 else 0


def clear_screen():
    """
    Clears the terminal screen for the game to be prettier
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def random_even_number(min, max):
    while True:
        line = random.randint(min, max)
        if line % 2 == 0:
            break
        else: continue
    return line


def random_odd_number(min, max):
    while True:
        line = random.randint(min, max)
        if line % 2 == 0:
            continue
        else: break
    return line
