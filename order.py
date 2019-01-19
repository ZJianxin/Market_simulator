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
    Counter = 0
    def __init__(self, arg1, price == None, remaining == None):
        #input: a numpy array,
        Counter += 1
        self.id = Counter
        if array.shape[0] == 4:
            #in this case, the initilzed Order object is an initial order
            #i.e. this order exits by the start of time frame
            self.is_bid = (array[0] == 1)
            self.price = array[2]
            self.remainming =  array[3]
            self.is_dead = False
            self.borntime = 0
            self.dead_time = float("inf")
        else if array.shape[0] = 7:
            self.is_bid = (array[0] == 1)
            self.price = array[1]
            self.