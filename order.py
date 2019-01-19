import numpy as np
from update import Update

class Order:
    #Static variable: counter - count the total number of existed orders.
    #
    #Attributes:
    #   id - int, unique id for each order.
    #   price - float, the price of this order.
    #   remaining - float, the remaining trading volume.
    #   is_bid - bool, true if this order is a bid order; false otherwise.
    #   is_dead - bool, true if this order's volume is zero or the order is cancelled; false otherwise.
    #   born_time - int, interpreted in milliseconds, the time when the order comes into existence;
    #             all initial orders will be marked with the same timestamp 0.
    #   dead_time - int or float("inf"), interpreted int milliseconds, the time when the remaining volume of order becomes zero
    #
    #Methods:
    #   initializer - initialize an order from an Update object or a 1-d numpy array
    #   mofify - modify the order object given an Update object
    #   *getters - return value of attributes
    Counter = 0
    def __init__(self, array):
        #Construct an Order object
        #Input: a numpy array, or an Update object
        #Returns:
        #Modifies:
        self.id = Order.Counter
        Order.Counter += 1
        if isinstance(array, np.ndarray):
            assert (array.shape[0] == 3)
            #in this case, the initilzed Order object is an initial order
            #i.e. this order exits by the start of time frame
            self.is_bid = (array[0] == 1)
            self.price = array[1]
            self.remainming =  array[2]
            self.is_dead = False
            self.birthtime = 0
            self.deathtime = float("inf")
        else:
            update = array
            assert (isinstance(update, Update))
            assert (update.get_reason() == 2)
            assert (update.get_remaining() == update.get_delta())
            self.is_bid = update.get_is_bid()
            self.price = update.get_price()
            self.remainming = update.get_remaining()
            self.is_dead = False
            self.birthtime = update.get_timestamp()
            self.deathtime = float("inf")


    def get_id(self):
        return self.id

    def get_is_bit(self):
        return self.is_bid

    def get_price(self):
        return self.price

    def get_remaining(self):
        return self.remainming

    def get_is_dead(self):
        return self.is_dead

    def get_borntime(self):
        return self.birthtime

    def get_deathtime(self):
        #if the order is still living, return float("inf")
        return self.deathtime

    def modify(self, update):
        assert (update.get_reason() == 1 or update.get_reason() == 2)
        if (update.get_reason() == 1):
            #this order is cancelled
            assert (update.get_delta() == 0 and update.get_remaining == 0 and update.get_price() == self.get_price())
            self.remainming == 0
            self.is_dead = True
            self.deathtime = update.get_timestamp()
        elif (update.get_reason() == 2):
            #this order is traded, partially or completely
            assert (update.get_price() == self.get_price())
            self.remainming = update.get_remainming()
            if (self.remainming == 0):
                self.is_dead = True
                self.deathtime = update.get_timestamp()
