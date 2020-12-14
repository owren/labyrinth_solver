
from values.Direction import Direction
from values.Path import Path
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
        self.__solved = False

    def depth_first_search(self, y_coordinate, x_coordinate, surface):
        current_y = y_coordinate
        current_x = x_coordinate
        while not self.__solved:

            if [current_y, current_x] not in self.__stack:
                self.add_to_stack_and_visualize(current_y, current_x, surface)
            cell = self.__maze[current_y, current_x]

            if not cell.get_wall(Direction.NORTH) and not self.__solved:
                if current_y - 1 < 0:
                    self.__solved = True
                    break
                next_cell = self.__maze[current_y - 1, current_x]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y - 1
                    current_x = current_x
                    continue

            if not cell.get_wall(Direction.EAST) and not self.__solved:
                if current_x + 1 > self.__maze.shape[1] - 1:
                    self.__solved = True
                    break
                next_cell = self.__maze[current_y, current_x + 1]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y
                    current_x = current_x + 1
                    continue

            if not cell.get_wall(Direction.SOUTH) and not self.__solved:
                if current_y + 1 > self.__maze.shape[0] - 1:
                    self.__solved = True
                    break
                next_cell = self.__maze[current_y + 1, current_x]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y + 1
                    current_x = current_x
                    continue

            if not cell.get_wall(Direction.WEST) and not self.__solved:
                if current_x - 1 < 0:
                    self.__solved = True
                    break
                next_cell = self.__maze[current_y, current_x - 1]
                if next_cell.get_used() == Path.NO:
                    current_y = current_y
                    current_x = current_x - 1
                    continue

            if not self.__solved:
                self.pop_off_stack_and_visualize(current_y, current_x, surface)
                current_y = self.__stack[-1][0]
                current_x = self.__stack[-1][1]

    def recursive_backtracking(self, current_y, current_x, surface):
        self.add_to_stack_and_visualize(current_y, current_x, surface)
        #print(len(self.__stack))
        # gets the current cell
        cell = self.__maze[current_y, current_x]

        if not cell.get_wall(Direction.NORTH) and not self.__solved:
            if current_y - 1 < 0:
                self.__solved = True
                return
                # found goal
            next_cell = self.__maze[current_y - 1, current_x]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y - 1, current_x, surface)

        if not cell.get_wall(Direction.EAST) and not self.__solved:
            if current_x + 1 > self.__maze.shape[1] - 1:
                self.__solved = True
                return
            next_cell = self.__maze[current_y, current_x + 1]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y, current_x + 1, surface)

        if not cell.get_wall(Direction.SOUTH) and not self.__solved:
            if current_y + 1 > self.__maze.shape[0] - 1:
                self.__solved = True
                return
            next_cell = self.__maze[current_y + 1, current_x]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y + 1, current_x, surface)

        if not cell.get_wall(Direction.WEST) and not self.__solved:
            if current_x - 1 < 0:
                self.__solved = True
                return
            next_cell = self.__maze[current_y, current_x - 1]
            if next_cell.get_used() == Path.NO:
                self.recursive_backtracking(current_y, current_x - 1, surface)

        # set other color and pop off stack
        if not self.__solved:
            self.pop_off_stack_and_visualize(current_y, current_x, surface)
        else:
            return

    def add_to_stack_and_visualize(self, y_coordinate, x_coordinate, surface):
        self.__stack.append([y_coordinate, x_coordinate])
        self.visualize_rectangle(y_coordinate, x_coordinate, surface, Path.YES, GREEN)

    def pop_off_stack_and_visualize(self, y_coordinate, x_coordinate, surface):
        self.__stack.pop()
        self.visualize_rectangle(y_coordinate, x_coordinate, surface, Path.WAS, RED)

    def visualize_rectangle(self, y_coordinate, x_coordinate, surface, path, colour):
        self.__maze[y_coordinate, x_coordinate].set_used(path)
        y_0 = y_coordinate * self.__cell_size + PADDING
        y_1 = (y_coordinate + 1) * self.__cell_size + PADDING
        x_0 = x_coordinate * self.__cell_size + PADDING
        x_1 = (x_coordinate + 1) * self.__cell_size + PADDING
        draw_rect(surface, colour, x_0, y_0, x_1, y_1, self.__cell_size)

    def get_stack(self):
        return self.__stack
