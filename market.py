from orderbook import *
from update import *
import numpy as np
import copy
from os import listdir
from os.path import isfile, join
from bisect import bisect_left

class Market:
    # simulate transactions in the market, calculate the orderbook at a given time
    # Attributes:
    #   initial_orderbook - the orderbook storing the initial orders by the beginning of inspection
    #   current_orderbook - an orderbook object storing current orderbook, if need to recaculate, use reset()
    #   updates_matrix - a numpy array containing the information of updates in the form of matrix
    # Methods:
    #   initializer - construct the initial orderbook
    #   calculate_orderbook - calculate an orderbook using all updates before a given timestamp
    def __init__(self, order_data, update_data, order_dir):
        # construct a market object, initialize the orderbook, store the update matrix
        # Input:
        #   order_date - a numpy array with desired format
        #   update_date - a numpy array with desired format
        # Returns:
        # Modifies:
        assert (isinstance(order_data, np.ndarray) and isinstance(update_data, np.ndarray))
        self.initial_orderbook = Orderbook(order_data)
        self.current_orderbook = Orderbook(order_data)
        self.updates_matrix = update_data
        self.updates_counter = 0
        self.malicious_updates_counter = 0
        self.time = 0
        self.order_dir = order_dir
        files = [f for f in listdir(self.order_dir) if isfile(join(self.order_dir, f))]
        self.files = sorted(files)
        self.files_num = [int(f[:-4]) for f in sorted(files)]
        self.closest_prior = 0

    def calculate_orderbook(self, time):
        # calculate an orderbook at the given time
        # Input:
        #   time - an integer representing the time of inspection
        # Returns:
        #   an orderbook object
        # Modifies:
        #orderbook = copy.deepcopy(self.initial_orderbook)
        next_update = Update(self.updates_matrix[max(self.updates_counter - 1, 0), :])
        if time < self.time:
            print("query a time later than", self.time)
            print("or use 'reset' to reset the orderbook")
            raise INVALID_TIME("INVALID TIME")

        #load from file
        if self.order_dir != None:
            query_prior = bisect_left(self.files_num, time) - 1
            jump_time = self.files_num[query_prior]
            if query_prior > self.closest_prior:
                self.closest_prior = query_prior
                order = np.load(self.order_dir + '/' + self.files[query_prior])
                self.reload(order, jump_time)
                while next_update.get_timestamp() < time:
                    self.updates_counter += 1
                    next_update = Update(self.updates_matrix[self.updates_counter, :])

        while (next_update.get_timestamp() < time and self.updates_counter < self.updates_matrix.shape[0]):
            next_update = Update(self.updates_matrix[self.updates_counter, :])
            try:
                self.current_orderbook.execute_update(next_update)
            except:
                print("malicious update found at time", next_update.get_timestamp())
                self.malicious_updates_counter += 1
            self.updates_counter += 1
        self.time = time
        return self.current_orderbook

    def reset(self):
        #reset the orderbook to time 0
        self.current_orderbook = copy.deepcopy(self.initial_orderbook)
        self.updates_counter = 0
        self.malicious_updates_counter = 0
        self.time = 0

    def get_num_malicious(self):
        #return the number of malicious updates
        return self.malicious_updates_counter

    def print_num_malicious(self):
        #return the number of malicious updates
        print("found abnormal updates:", self.malicious_updates_counter)

    def reload(self, order_data, jump_time):
        self.current_orderbook = Orderbook(order_data)
        print("orderbook at", self.time, "jump to orderbook reloaded from dataset at", jump_time)