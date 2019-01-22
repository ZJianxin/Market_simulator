class Update:
    # Attributes:
    #   id - int, the event id
    #   is_bid - bool, the value of self.is_bid attribute of corresponding order
    #   price - float, the value of self.price attribute of corresponding order
    #   remaining - float, the remaining volume of corresponding order after the update
    #   delta - float, the change of remaining volume
    #   timestamp - int, an int representing the time (in millisecond)
    #   reason - int, the reason of the change, 3 possible values.
    # Methods:
    #   initializer - initialize an Update object from a 1-d numpy array OR 7 arguments (same ordering)
    #   getters - return each attribute, name: get_<variable name>

    # Input:
    #   file - file name of the numpy array of the update information
    #   i - read the ith entry
    # Modifies:
    #   setting the initial 7 arguments

    def __init__(self, update_entry):
        self.is_bid = update_entry[0]
        self.price = update_entry[1]
        self.remaining = update_entry[2]
        self.delta = update_entry[3]
        self.timestamp = update_entry[5]
        self.reason = update_entry[6]
        self.id = update_entry[7]

    # Returns:
    #   is_bid
    def get_is_bid(self):
        return self.is_bid == 1

    # Returns:
    #   price
    def get_price(self):
        return self.price

    # Returns:
    #   remaining volume
    def get_remaining(self):
        return self.remaining

    # Returns:
    #   delta
    def get_delta(self):
        return self.delta

    # Returns:
    #   timestamp
    def get_timestamp(self):
        return int(self.timestamp)

    # Returns:
    #   reason
    def get_reason(self):
        return int(self.reason)

    # Return:
    #   eventId
    def get_id(self):
        return int(self.id)

    def round_remaining(self, n=12):
        self.remaining = round(self.remaining, n)

    def round_delta(self, n):
        self.delta = round(self.delta, n)

'''
Sample function comment:

def func(arg1, arg2 == Default):
    #(state function behavior)
    #Input: 
    #   arg1 - type1, (explanation) || type2, (explanation) || ...
    #   arg2 - ...
    #Returns:
    #   output - (explanation)
    #Modifies: 
    #   variable_name - type, (explanation)

'''
