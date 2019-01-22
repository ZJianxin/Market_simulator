import sys
import numpy
from market import *

def main():
    initial_order_file = sys.argv[0]
    updates_file = sys.argv[1]
    initial_order_matrix = numpy.load(initial_order_file)
    updates_matrix = numpy.load(updates_file)
    market = Market(initial_order_matrix, updates_matrix)
    time = 0
    while (True):
        time = input("Type the time you'd like to query, -1 for exit")
        if (time == -1):
            break
        ob = market.calculate_orderbook(time)
        ob.show_head()
    return 0


if __name__ == '__main__':
   main()