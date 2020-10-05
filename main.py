################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from Board_old import Board as Board_old
from robust_IO import input_int


def main():
    #vertical = int(input('Vertical size: '))
    #horizontal = int(input('Horizontal size: '))
    #y_coordinate = int(input('Y-coordinate for starting point: '))
    #x_coordinate = int(input('X-coordinate for starting point: '))
    from datetime import datetime
    startTime = datetime.now()
    a = Board(vertical=200, horizontal=200)
    print(datetime.now() - startTime)
    a.display_board()


if __name__ == "__main__":
    main()
