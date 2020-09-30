################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

from game_logic.Board import Board
from robust_IO import input_int


def main():
    from datetime import datetime
    startTime = datetime.now()
    a = Board(21, 21)
    print(datetime.now() - startTime)
    a.display_board()

if __name__ == "__main__":
    main()
