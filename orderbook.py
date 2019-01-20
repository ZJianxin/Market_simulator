from order import *
import numpy as np
import bisect
from sortedcontainers import SortedList


class Orderbook:
    #keeps a set of orders
    #represents a snapshot at a given time
    #Attributes:
    # keeps a set of orders
    # represents a snapshot at a given time
    # Attributes:
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
    # Methods:
    # public:
    #   initializer(Orderbook, np.ndarray, [optional] int timestamp) - initialize an Orderbook object from a number ndarray
    #   execute_update(Orderbook, Update) - update an order and time stamp, can't execute an order before timestamp
    #   ?todo: *design method allow information retrieval
    # private:
    #   _remove_order(Orderbook self, int id) - remove from order_dict, price_volume_dict, ask_list, bid_list
    #   _cancel_order(Orderbook self, Update update) - match order; remove it
    #   _trade_order(Orderbook self, Update update) - guaranteed to trade the "best order"; rehash/remove it if necessary
    #   _place_order(Orderbook self, Update update) - create an new Order object; hash into order_dict and price_volume_dict;
    #                         insert into ask_list and bid_list
    #!!!!!!!!!rememeber update timestamp
    def __int__(self, data, timestamp = 0):
        #Input: a numpy ndarray, formatted as desired initial orders
        #Returns:
        #Modifies:
        #   Initialize an orderbook object
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

    def _remove_order(self, id):
        #remove the order of given id from all containers in the Orderbook object
        #Input: id of the order to be removed
        #Returns:
        #Modifies:
        #   order_dict - remove the key from order_dict; order object retained.
        #   price_volume_dict - remove the key from price_volume_dict, order object retained.
        #   ask_list - remove the key from ask_list; order object retained; original order retained.
        #   bid_list - remove the key from bid_list; order object retained; original order retained.
        order = self.order_dict[id]
        price_volume_pair = (order.get_price(), order.get_remaining())
        assert (price_volume_pair in self.price_volume_dict.keys()
                and len(self.price_volume_dict[price_volume_pair]) > 0, "INVALID PRICE_VOLUME_PAIR KEY")
        #if len(self.price_volume_dict[price_volume_pair] == 1):
        #    del self.price_volume_dict[price_volume_pair]
        self.price_volume_dict[price_volume_pair].remove(id)
        if (order.get_is_bit()):
            self.bid_list.remove(id)
        else:
            self.ask_list.remove(id)
        self.order_dict.pop(id)

    def _cancel_order(self, update):
        #cancel an order with corresponding (price, volume) pair with the update Object.
        #If multiple orders with the same key exist, the one with SMALLEST birthtime value will be cancelled
        #Input: an Update object;
        #       assume update.reason = 1, i.e. the "reason" attribute of update should be "cancel"
        #Returns:
        #Modifies:
        #   the value of (price, volume) key in self.price_volume_pair.
        #   order_dict - corresponding key will be removed by _remove_order
        #   price_volume_dict - corresponding key will be removed by _remove_order
        #   ask_list - corresponding id will be removed by _remove_order
        #   bidlist - corresponding id will be removed by _remove_order
        assert (update.reason == 1)
        pv_pair = (update.get_price(), update.get_remaining() - update.get_delta())
        assert (pv_pair in self.price_volume_dict.keys()
                and len(self.price_volume_dict[pv_pair]) > 0, "INVALID PRICE_VOLUME_PAIR KEY")
        id = self.price_volume_dict[pv_pair][0]
        self.order_dict[id].modify(update)
        self._remove_order(id)

    def _trade_order(self, update):
        # trade an order AT THE TOP OF ORDERBOOK. i.e either bid_list[0] or ask_list[0] will be modified
        # Input: an Update object;
        #       assume update.reason = 2, i.e. the "reason" attribute of update should be "trade"
        # Returns:
        # Modifies:
        #   the trading Order object.
        #   order_dict - corresponding key will be removed by _remove_order
        #   price_volume_dict - corresponding key will be removed by _remove_order
        #   ask_list - corresponding id will be removed by _remove_order
        #   bidlist - corresponding id will be removed by _remove_order

