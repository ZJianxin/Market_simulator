from order import *
import numpy as np
import bisect
from sortedcontainers import SortedList

class Orderbook:
    #keeps a set of orders
    #represents a snapshot at a given time
    #Attributes:
    #   timestamp - the time associated with the snapshot of market, automatically updated with latest order;
    #               it's the USER's responsibility to maintain its integrity
    #   order_dict - a dictionary mapping order_id to order, the container of Order objects
    #   price_volume_dict - a dictionary mapping a tuple (price, volume)
    #                                         to a list of SortedList IDs in increasing arrangement of order.birthtime
    #                       utilized to retrieve the corresponding order with cancel type,
    #                       delete the old key-value pair and rehash once an order has been modified.
    #   ask_list - a list of ask orders' id sorted by price in increasing order
    #   bid_list - a list of bid orders' id sorted by price in decrease order
    #              assume in each "trade" update, only best price be executed.
    #Methods:
    # public:
    #   initializer(Orderbook, np.ndarray, [optional] int timestamp) - initialize an Orderbook object from a number ndarray
    #   execute_update(Orderbook, Update) - update an order and time stamp, can't execute an order before timestamp
    #   ?todo: *design method allow information retrieval
    # private:
    #   remove_order(id) - remove from price_volume_dict, ask_list, bid_list
    #   cancel_order(Update) - match order; remove it
    #   trade_order(Update) - guaranteed to trade the "best order"; rehash/remove it if necessary
    #   place_order(Update) - create an new Order object; hash into order_dict and price_volume_dict;
    #                         insert into ask_list and bid_list

    #!!!!!!!!!rememeber update timestamp
    def __int__(self, data, timestamp = 0):
        self.timestamp = timestamp
        self.order_dict = {}
        self.price_volume_dict = {}
        self.ask_list = SortedList(key = lambda x, d=self.order_dict : d[x].get_price())
        self.bid_list = SortedList(key = lambda x, d=self.order_dict : -d[x].get_price())
        for i in range(data.shape[0]):
            order = Order(data[i, :])
            id = order.get_id()
            self.order_dict[id] = order
            #self.price_volume_dict[(order.get_price(), order.get_remaining())] = order.get_id()
            price_volume_pair = (order.get_price(), order.get_remaining())
            if (price_volume_pair in self.price_volume_dict.keys()):
                self.price_volume_dict[price_volume_pair].add(id)
            else:
                self.price_volume_dict[price_volume_pair] = SortedList(key = lambda x, d=self.order_dict : d[x].get_birthtime())
                self.price_volume_dict[price_volume_pair].add(id)
            if (order.get_is_bit()):
                self.bid_list.add(id)
            else:
                self.ask_list.add(id)

