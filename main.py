import sys
import numpy
from market import *

def main(argv):
    initial_order_file = argv[0]
    updates_file = argv[1]
    initial_order_matrix = numpy.load(initial_order_file)
    updates_matrix = numpy.load(updates_file)
    #todo: better ways to fix precision matter
    for i in range(initial_order_matrix.shape[0]):
        initial_order_matrix[i, 1] = round(initial_order_matrix[i, 1], 12)
        initial_order_matrix[i, 2] = round(initial_order_matrix[i, 2], 12)
    for i in range(updates_matrix.shape[0]):
        updates_matrix[i, 2] = round(updates_matrix[i, 2], 12)
        updates_matrix[i, 3] = round(updates_matrix[i, 3], 12)
    ##################################
    print(updates_matrix[729])
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