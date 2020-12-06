################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from Board_old import Board as Board_old
from robust_IO import input_int


import pygame

"""
# set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 30

# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)

# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()
"""
def main():
    #vertical = int(input('Vertical size: '))
    #horizontal = int(input('Horizontal size: '))
    #y_coordinate = int(input('Y-coordinate for starting point: '))
    #x_coordinate = int(input('X-coordinate for starting point: '))
    from datetime import datetime
    startTime = datetime.now()
    a = Board(vertical=50, horizontal=50)
    print(datetime.now() - startTime)
    a.display_board()


if __name__ == "__main__":
    main()
