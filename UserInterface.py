import tkinter as tk

import pygame

from values import Constants
import visualization
from MazeSolver import MazeSolver
from maze.Board import Board

tk_width = 300
tk_height = 200


class UserInterface:

    def __init__(self):
        self.initiate_tkinter()
        #self.initiate_pygame()

    def initiate_tkinter(self):
        root = tk.Tk()
        root.title('Maze Solver Options')

        #root.geometry(str(tk_width) + 'x' + str(tk_height))
        self.tk_inputs(root)

        root.mainloop()

    def tk_inputs(self, root):
        tk.Label(root, text='Options').grid(row=1, column=1, columnspan=3)
        tk.Label(root, text='          ').grid(row=2, column=2)

        tk.Label(root, text='No of vertical cells').grid(row=2, column=1)
        self.__vertical = tk.Scale(root, from_=2, to=Constants.NO_OF_V_CELLS, orient=tk.HORIZONTAL, command=self.__vertical_callback)
        self.__vertical.grid(row=2, column=3)

        tk.Label(root, text='No of horizontal cells').grid(row=3, column=1)
        self.__horizontal = tk.Scale(root, from_=2, to=self.__vertical.get() * 2, orient=tk.HORIZONTAL, command=self.__horizontal_callback)
        self.__horizontal.grid(row=3, column=3)

        tk.Label(root, text='Y-coordinate starting point').grid(row=4, column=1)
        self.__y_coordinate_start = tk.Scale(root, from_=0, to=self.__vertical.get() - 1, orient=tk.HORIZONTAL, command=self.__y_coordinate_callback)
        self.__y_coordinate_start.grid(row=4, column=3)

        tk.Label(root, text='X-coordinate starting point').grid(row=5, column=1)
        self.__x_coordinate_start = tk.Scale(root, from_=0, to=self.__horizontal.get() - 1, orient=tk.HORIZONTAL, command=self.__x_coordinate_callback)
        self.__x_coordinate_start.grid(row=5, column=3)

        tk.Label(root, text="Show Animation").grid(row=6, column=1)
        self.__show_animation = tk.BooleanVar()
        self.__animation_check = tk.Checkbutton(root, variable=self.__show_animation, command=self.__show_animation_callback).grid(row=6, column=3)

        tk.Button(root, text="START", command=self.__start_game, bg='black', fg='white').grid(row=7, column=1, columnspan=3)

    def __vertical_callback(self, value):
        self.__tk_vertical_ = int(value)
        self.__horizontal.configure(to=int(value) * 2)
        self.__y_coordinate_start.configure(to=int(value) - 1)

    def __horizontal_callback(self, value):
        self.__tk_horizontal_ = int(value)
        self.__x_coordinate_start.configure(to=int(value) - 1)

    def __y_coordinate_callback(self, value):
        self.__y_coordinate_start_ = int(value)

    def __x_coordinate_callback(self, value):
        self.__x_coordinate_start_ = int(value)

    def __show_animation_callback(self):
        self.__show_animation_ = self.__show_animation.get()

    def __start_game(self):
        rows = self.__tk_vertical_
        columns = self.__tk_horizontal_
        y_coordinate = self.__y_coordinate_start_
        x_coordinate = self.__x_coordinate_start_

        height = int(Constants.V_SIZE)
        width = int((height / rows) * columns)
        cell_size = int(height / rows)

        pygame.init()
        surface = pygame.display.set_mode((width + (Constants.PADDING * 2), height + (Constants.PADDING * 2)))
        pygame.display.set_caption('Maze Solver')
        surface.fill(Constants.GREY)

        text_surface = pygame.font.SysFont('calibri', 30).render('Generating maze, please wait...', False, Constants.BLACK)
        surface.blit(text_surface, (10, 10))
        pygame.display.update()
        maze = Board(vertical=rows, horizontal=columns, size=[height, width])

        visualization.draw_maze(maze.get_board(), cell_size, surface)

        solver = MazeSolver(maze.get_board(), cell_size, [y_coordinate, x_coordinate], surface)

        solver.depth_first_search(y_coordinate, x_coordinate, surface)

        stack = solver.get_stack()
        pygame.display.update()
        visualization.run_loop()


