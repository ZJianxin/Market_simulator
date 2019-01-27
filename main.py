import sys
import numpy
from market import *

def main(argv):
    initial_order_file = argv[0]
    updates_file = argv[1]
    initial_order_matrix = numpy.load(initial_order_file)
    updates_matrix = numpy.load(updates_file)
    # DEBUG CODE
    '''
    for i in range(initial_order_matrix.shape[0]):
        if (abs(initial_order_matrix[i, 2] - 1.04839784) < 1e-5):
            print('TRUE')
            exit(1)
    for i in range(53792):
        if (abs(updates_matrix[i, 2] - 1.04839784) < 1e-5):
            print('TRUE')
            exit(1)
    print('NOT EXIST')
    exit(2)
    '''
    market = Market(initial_order_matrix, updates_matrix)
    while (True):
        time = int(input("Type the time you'd like to query, -1 for exit : \n"))
        if (time == -1):
            break
        ob = market.calculate_orderbook(time)
        ob.show_head()
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])