from order import *
import numpy as np
import bisect


class Orderbook:
    # keeps a se of orders
    # represents a snapshot at a given time
    # Attributes:
    #   timestamp - the time associated with the snapshot of market, automatically updated with latest order;
    #               it's the USER's responsibility to maintain its integrity
    #   order_dict - a dictionary mapping order_id to order, container of orders
    #   price_volume_dict - a dictionary mapping a tuple of (price, volume) to an order id,
    #                       utilized to retrieve the corresponding order with cancel type,
    #                       delete the old key-value pair and rehash once an order has been modified.
    #   ask_list - a list of ask orders' id sorted by price in increasing order
    #   bid_list - a list of bid orders' id sorted by price in decrease order
    #              assume in each "trade" update, only best price be executed.
    # Methods:
    # public:
    #   initializer(Orderbook, np.ndarray) - initialize an Orderbook object from a number ndarray
    #   execute_update(Orderbook, Update) - update an order and time stamp
    #   ?todo: *design method allow information retrieval
    # private:
    #   remove_order(id) - remove from price_volume_dict, ask_list, bid_list
    #   cancel_order(Update) - match order; remove it
    #   trade_order(Update) - guaranteed to trade the "best order"; rehash/remove it if necessary
    #   place_order(Update) - create an new Order object; hash into order_dict and price_volume_dict;
    #                         insert into ask_list and bid_list

    # !!!!!!!!!remember update timestamp
    def __int__(self):
        pass
