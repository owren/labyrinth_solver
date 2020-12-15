import tkinter as tk
import pygame
from pygame.locals import KEYDOWN, K_q
import sys

from maze.MazeGenerator import MazeGenerator
from maze.MazeSolver import MazeSolver
from values import Constants
from maze.Board import Board


class UserInterface:

    def __init__(self):
        self.__rows = Constants.ROWS
        self.__columns = Constants.COLUMNS
        self.__y_coordinate = Constants.Y_START
        self.__x_coordinate = Constants.X_START
        self.__animation = True
        self.root = self.__initiate_ui()
        self.__surface = self.__initiate_pygame()

    def run_loop(self):
        while True:
            try:
                self.root.update()
            except tk.TclError:
                sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.root.destroy()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_q:
                    self.root.destroy()
                    pygame.quit()
                    sys.exit()

    def __initiate_ui(self):
        root = tk.Tk()
        root.title('Maze Solver')
        self.__ui_inputs(root)
        return root

    def __initiate_pygame(self):
        pygame.display.init()
        surface = pygame.display.set_mode((100, 1))
        return surface

    def __ui_inputs(self, root):
        tk.Label(root, text='Options').grid(row=1, column=1, columnspan=3)
        tk.Label(root, text='          ').grid(row=2, column=2)

        tk.Label(root, text="Use Smaller Slider").grid(row=2, column=1)
        self.__smaller_slider = tk.BooleanVar()
        self.__smaller_slider.set(True)
        self.__smaller_check = tk.Checkbutton(root, variable=self.__smaller_slider, command=self.__smaller_slider_callback).grid(row=2, column=3)

        tk.Label(root, text='No of vertical cells').grid(row=3, column=1)
        self.__vertical = tk.Scale(root, from_=2, to=Constants.NO_OF_V_CELLS / 10, orient=tk.HORIZONTAL, command=self.__vertical_callback)
        self.__vertical.set(self.__rows)
        self.__vertical.grid(row=3, column=3)

        tk.Label(root, text='No of horizontal cells').grid(row=4, column=1)
        self.__horizontal = tk.Scale(root, from_=2, to=self.__vertical.get() * 2, orient=tk.HORIZONTAL, command=self.__horizontal_callback)
        self.__horizontal.set(self.__columns)
        self.__horizontal.grid(row=4, column=3)

        tk.Label(root, text='Y-coordinate starting point').grid(row=5, column=1)
        self.__y_coordinate_start = tk.Scale(root, from_=0, to=self.__vertical.get() - 1, orient=tk.HORIZONTAL, command=self.__y_coordinate_callback)
        self.__y_coordinate_start.set(self.__y_coordinate)
        self.__y_coordinate_start.grid(row=5, column=3)

        tk.Label(root, text='X-coordinate starting point').grid(row=6, column=1)
        self.__x_coordinate_start = tk.Scale(root, from_=0, to=self.__horizontal.get() - 1, orient=tk.HORIZONTAL, command=self.__x_coordinate_callback)
        self.__x_coordinate_start.set(self.__x_coordinate)
        self.__x_coordinate_start.grid(row=6, column=3)

        tk.Label(root, text="Show Animation").grid(row=7, column=1)
        self.__show_animation = tk.BooleanVar()
        self.__show_animation.set(True)
        self.__animation_check = tk.Checkbutton(root, variable=self.__show_animation, command=self.__show_animation_callback).grid(row=7, column=3)

        tk.Label(root).grid(row=8, column=1)
        tk.Button(root, text="START", command=self.__start_game, bg='black', fg='white').grid(row=9, column=1, columnspan=3)
        tk.Label(root).grid(row=10, column=1)

    def __smaller_slider_callback(self):
        if self.__smaller_slider.get():
            self.__vertical.configure(to=int(Constants.NO_OF_V_CELLS / 10))
            self.__horizontal.configure(to=int(self.__vertical.get() * 2))
        else:
            self.__vertical.configure(to=int(Constants.NO_OF_V_CELLS))
            self.__horizontal.configure(to=int(self.__vertical.get() * 2))

    def __vertical_callback(self, value):
        self.__rows = int(value)
        self.__horizontal.configure(to=int(value) * 2)
        self.__y_coordinate_start.configure(to=int(value) - 1)

    def __horizontal_callback(self, value):
        self.__columns = int(value)
        self.__x_coordinate_start.configure(to=int(value) - 1)

    def __y_coordinate_callback(self, value):
        self.__y_coordinate = int(value)

    def __x_coordinate_callback(self, value):
        self.__x_coordinate = int(value)

    def __show_animation_callback(self):
        self.__animation = self.__show_animation.get()

    def __start_game(self):
        cell_size = int(Constants.V_MAX / self.__rows)
        height = cell_size * self.__rows
        width = cell_size * self.__columns
        board = Board(self.__rows, self.__columns, height, width, cell_size)

        generator = MazeGenerator(board.get_board(), cell_size, animation=self.__animation)
        surface = generator.generate(height=height, width=width)

        solver = MazeSolver(board.get_board(), cell_size, animation=self.__animation)
        solver.depth_first_search(self.__y_coordinate, self.__x_coordinate, surface)
        pygame.display.update()
