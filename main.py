################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from Board import Board
from Board_old import Board as Board_old
from robust_IO import input_int


def main():
    from datetime import datetime
    startTime = datetime.now()
    a = Board(20, 20)
    print(datetime.now() - startTime)
    a.display_board()


if __name__ == "__main__":
    main()
