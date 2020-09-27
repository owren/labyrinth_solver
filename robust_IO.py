################################################################################
# Pål Anders Wangen Owren                                                      #
# Student nummer: 333704                                                       #
################################################################################

################################################################################
# This file is written to make sure the user doesn't type anything wrong       #
################################################################################


def input_int(text, min=0, max=999999):
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
            if inp in range (min, max + 1):
                return inp
            else:
                print('Input has to be between', min, 'and', max, '\n')
                continue
    return inp
