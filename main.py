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
    price = 3426.22
    volume = 2.92346414
    for i in range(initial_order_matrix.shape[0]):
        if (abs(initial_order_matrix[i, 2] - volume) < 1e-5):
            print('TRUE')
            exit(1)
    for i in range(updates_matrix.shape[0]):
        if (abs(updates_matrix[i, 2] - volume) < 1e-5):
            print('TRUE')
            exit(1)
    print('NOT EXIST')
    exit(2)
    '''
    '''
    price = 3426.22
    volume = 3.0
    initial_counter = 0
    update_counter = {}
    update_counter[1] = 0
    update_counter[2] = 0
    update_counter[3] = 0
    time = 1549130255361
    for i in range(initial_order_matrix.shape[0]):
        if (initial_order_matrix[i, 1] == price):
            initial_counter += 1
    for i in range(updates_matrix.shape[0]):
        type = updates_matrix[i, 6]
        if (updates_matrix[i, 1] == price and updates_matrix[i, 4] <= time):
            print(updates_matrix[i, :])
            print()
            update_counter[type] += 1
    print(initial_counter, update_counter)
    exit(1)
    '''
    ##########
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
