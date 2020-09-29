################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

import random
import os
import time

VER, HOR = 0, 1

def decide_orientation(width, height):
    if width < height:
        return HOR
    elif width > height:
        return VER
    else:
        return HOR if random.randint(0, 1) == 0 else VER


def clear_screen():
    """
    Clears the terminal screen for the game to be prettier
    """
    wait(.5)
    os.system('cls' if os.name == 'nt' else 'clear')


def wait(x):
    time.sleep(x)


def random_even_number(min, max):
    while True:
        line = random.randint(min + 1, max)
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


def print_orientation(ori):
    if ori == VER:
        print('ver')
    else: print('hor')