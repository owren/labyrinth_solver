################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

################################################################################
# This file is written to make sure the user doesn't type anything wrong       #
################################################################################


def input_int(text, minimum=0, maximum=999999):
    """
    Make sure an integer input is actually an integer
    """
    while True:
        try:
            inp = int(input(text))
        except ValueError:
            print('Input should be an integer, try again! \n')
            continue
        else:
            if inp in range(minimum, maximum + 1):
                return inp
            else:
                print('Input has to be between', minimum, 'and', maximum, '\n')
                continue
