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
    price = 3618.86
    volume = 1.04839784
    init_counter = 0
    update_counter = 0
    for i in range(initial_order_matrix.shape[0]):
        if (abs(initial_order_matrix[i, 2] - volume) < 1e-3):
            init_counter += 1
    for i in range(updates_matrix.shape[0]):
        if (abs(updates_matrix[i, 2] - volume) < 1e-3):
            update_counter += 1
            print(updates_matrix[i, :])
    print('occurrences in init:', init_counter, )
    print('occurrences in update:', update_counter)
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
        command = input("Type the time you'd like to query, -1, or 'reset' : \n")
        if (command == "-1"):
            break
        elif (command == "reset"):
            market.reset()
        elif (command == ""):
            continue;
        else:
            try:
                time = int(command)
                ob = market.calculate_orderbook(time)
                ob.show_head()
                market.print_num_malicious()
            except:
                continue;
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])
