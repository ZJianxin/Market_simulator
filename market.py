from orderbook import *
from update import *
import numpy as np
import copy

class Market:
    # simulate transactions in the market, calculate the orderbook at a given time
    # Attributes:
    #   initial_orderbook - the orderbook storing the initial orders by the beginning of inspection
    #   updates_matrix - a numpy array containing the information of updates in the form of matrix
    # Methods:
    #   initializer - construct the initial orderbook
    #   calculate_orderbook - calculate an orderbook using all updates before a given timestamp
    def __int__(self, order_data, update_date):
        # construct a market object, initialize the orderbook, store the update matrix
        # Input:
        #   order_date - a numpy array with desired format
        #   update_date - a numpy array with desired format
        # Returns:
        # Modifies:
        assert (isinstance(order_data, np.ndarray) and isinstance(update_date, np.ndarray))
        self.initial_orderbook = Orderbook(order_data)
        self.updates_matrix = update_date
        self.next_update_index =

    def calculate_orderbook(self, time):
        # calculate an orderbook at the given time
        # Input:
        #   time - an integer representing the time of inspection
        # Returns:
        #   an orderbook object
        # Modifies:
        orderbook = copy.deepcopy(self.initial_orderbook)
        i = 0
        next_update = Update(self.updates_matrix[i, :])
        while (next_update.get_timestamp() < time):
            orderbook.execute_update(next_update)
        return orderbook
