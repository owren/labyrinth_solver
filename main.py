################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from robust_IO import input_int
from Constants import *
import visualization
from MazeSolver import MazeSolver
from functions import recursionlimit
import sys

import pygame
import tkinter as tk


def main():
    """
    r = tk.Tk()
    r.title('Maze Solver setup')
    #button = tk.Button(r, text='Stop', width=25, command=r.destroy)
    #button.pack()
    tk.Label(r, text='No of vertical cells').grid(row=0)
    vertical = tk.IntVar()
    e1 = tk.Entry(r, textvariable=vertical, justify=tk.RIGHT)
    e1.grid(row=0, column=1)

    tk.Label(r, text='No of horizontal cells').grid(row=1)
    horizontal = tk.IntVar()
    e2 = tk.Entry(r, textvariable=horizontal, justify=tk.RIGHT)
    e2.grid(row=1, column=1)

    tk.Label(r, text='Y coordinate start').grid(row=2)
    y_start = tk.IntVar()
    e3 = tk.Entry(r, textvariable=y_start, justify=tk.RIGHT)
    e3.grid(row=2, column=1)

    tk.Label(r, text='X coordinate start').grid(row=3)
    x_start = tk.IntVar()
    e4 = tk.Entry(r, textvariable=y_start, justify=tk.RIGHT)
    e4.grid(row=3, column=1)

    tk.Label(r, text='Fast solver').grid(row=4)
    fast = tk.BooleanVar()
    c1 = tk.Checkbutton(r, text="Music", variable=fast)
    c1.grid(row=4, column=1)

    #CheckVar1 = tk.IntVar()
    #C1 = tk.Checkbutton(r, text="Music", variable=CheckVar1).grid(row=2)


    r.mainloop()
    #print(vertical.get())
    #print(CheckVar1.get())

    """
    #rows = int(input('Vertical size: '))
    #columns = int(input('Horizontal size: '))
    #y_coordinate = int(input('Y-coordinate for starting point: '))
    #x_coordinate = int(input('X-coordinate for starting point: '))
    rows = 50
    columns = 100
    x_coordinate = int(columns / 2)
    y_coordinate = int(rows / 2)

    height = int(V_SIZE)
    width = int((height / rows) * columns)
    cell_size = int(height / rows)

    pygame.init()
    surface = pygame.display.set_mode((width + (PADDING * 2), height + (PADDING * 2)))
    pygame.display.set_caption('Maze Solver')
    surface.fill(GREY)

    text_surface = pygame.font.SysFont('calibri', 30).render('Generating maze, please wait...', False, BLACK)
    surface.blit(text_surface, (10, 10))
    pygame.display.update()
    maze = Board(vertical=rows, horizontal=columns, size=[height, width])
    # a.display_board()

    #pygame.time.wait(2000)

    visualization.draw_maze(maze.get_board(), cell_size, surface)

    solver = MazeSolver(maze.get_board(), cell_size, [y_coordinate, x_coordinate], surface)

    #with recursionlimit(5000):
    #    solver.recursive_backtracking(y_coordinate, x_coordinate, surface)
    solver.depth_first_search(y_coordinate, x_coordinate, surface)
    #for i, j in enumerate(stack):
    #    print(i, j)
    stack = solver.get_stack()
    pygame.display.update()
    visualization.run_loop()




if __name__ == "__main__":
    main()
