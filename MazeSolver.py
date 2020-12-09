
from Types import *
from Constants import *
from visualization import draw_rect

class MazeSolver:
    # depth search
    def __init__(self, maze, cell_size, starting_position, surface):
        """
        :param starting_position: list of y- and x-coordinate for starting position
        """
        self.__stack = []
        self.__maze = maze
        self.__cell_size = cell_size
        #self.__current_y_position = starting_position[0]
        #self.__current_x_position = starting_position[1]
        #self.surface = surface
        #while True:
        #    self.check_next(self.__current_y_position, self.__current_x_position, self.surface)
        #    pass
            # solve

    def recursive_backtracking(self, current_y, current_x, surface):
        self.add_to_stack_and_visualize(current_y, current_x, surface)
        # gets the current cell
        cell = self.__maze[current_y, current_x]
        if not cell.get_wall(Direction.NORTH):# and current_x > 0:
            if current_y - 1 < 0:
                print('finished')
                # found goal
            next_cell = self.__maze[current_y - 1, current_x]
            if next_cell.get_used() == Path.NO:
                #print('opp')
                self.recursive_backtracking(current_y - 1, current_x, surface)

        if not cell.get_wall(Direction.EAST):# and current_y < self.__maze.shape[0]:
            if current_x + 1 > self.__maze.shape[1] - 1:
                print('finished')
            next_cell = self.__maze[current_y, current_x + 1]
            if next_cell.get_used() == Path.NO:
                #print('høyre')
                self.recursive_backtracking(current_y, current_x + 1, surface)


        if not cell.get_wall(Direction.SOUTH):# and current_x < self.__maze.shape[1]:
            next_cell = self.__maze[current_y + 1, current_x]
            if current_y + 1 > self.__maze.shape[0] - 1:
                print('finished')
            if next_cell.get_used() == Path.NO:
                #print('ned')
                self.recursive_backtracking(current_y + 1, current_x, surface)


        if not cell.get_wall(Direction.WEST):# and current_y > 0:
            if current_x - 1 < 0:
                print('finished')
            next_cell = self.__maze[current_y, current_x - 1]
            if next_cell.get_used() == Path.NO:
                #print('venstre')
                self.recursive_backtracking(current_y, current_x - 1, surface)

        # set other color and pop off stack
        not_goal = True
        if not_goal:
            self.pop_off_stack_and_visualize(current_y, current_x, surface)

    def add_to_stack_and_visualize(self, y_coordinate, x_coordinate, surface):
        self.__stack.append([y_coordinate, x_coordinate])
        self.__maze[y_coordinate, x_coordinate].set_used(Path.YES)
        y_0 = y_coordinate * self.__cell_size + PADDING
        y_1 = (y_coordinate + 1) * self.__cell_size + PADDING
        x_0 = x_coordinate * self.__cell_size + PADDING
        x_1 = (x_coordinate + 1) * self.__cell_size + PADDING
        draw_rect(surface, GREEN, x_0, y_0, x_1, y_1, self.__cell_size)

    def pop_off_stack_and_visualize(self, y_coordinate, x_coordinate, surface):
        self.__stack.pop()
        self.__maze[y_coordinate, x_coordinate].set_used(Path.WAS)
        y_0 = y_coordinate * self.__cell_size + PADDING
        y_1 = (y_coordinate + 1) * self.__cell_size + PADDING
        x_0 = x_coordinate * self.__cell_size + PADDING
        x_1 = (x_coordinate + 1) * self.__cell_size + PADDING
        draw_rect(surface, RED, x_0, y_0, x_1, y_1, self.__cell_size)
