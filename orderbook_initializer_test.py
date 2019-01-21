from orderbook import *

# Create input nd array for data
N = 30
orderbook_info = np.zeros((N, 3))
for i in range(N):
    orderbook_info[i, 0] = (i+1) % 2 + 1
    orderbook_info[i, 1] = (i + 1) * 4.53
    orderbook_info[i, 2] = (i + 1) * 3.88 - 9

orderbook1 = Orderbook(orderbook_info)


# Test the initializer for orderbook
if orderbook1.timestamp != 0:
    raise Exception("orderbook_initializer test01 fail")

for i in range(orderbook_info.shape[0]):
    if orderbook1.order_dict[i] != np.array([(i+1) % 2 + 1, (i % 5 + 1) * 4.53, (i % 5 + 1) * 3.88 - 9]):
        raise Exception("orderbook_initializer order_dict ", i, " fail")
    if i not in orderbook1.price_volume_dict[((i % 5 + 1) * 4.53, (i % 5 + 1) * 3.88 - 9)]:
        raise Exception("orderbook_initializer price_volume_pair ", i, " fail")
    if (i+1) % 2 + 1 == 1:
        if i not in orderbook1.bid_list:
            raise Exception("orderbook_initializer is_bid list ", i, " fail")
    else:
        if i not in orderbook1.ask_list:
            raise Exception("orderbook_initializer is_ask list ", i, " fail")

# Test update for order book
# Test cancel order
# Cancel the first 10 order

N = 10
update_info = np.zeros((N, 8))
update_list = []
for i in range(N):
    update_info[i, 0] = i % 2
    update_info[i, 1] = (i + 1) * 4.53
    update_info[i, 2] = 0
    update_info[i, 3] = - (i + 1) * 3.88 + 9
    update_info[i, 5] = i + 79343
    update_info[i, 6] = 1
    update_info[i, 7] = i * 554

for i in range(update_info.shape[0]):
    update_list.append(Update(update_info[i, :]))

for i in range(len(update_list)):
    orderbook1.execute_update(update_list[i])
    if i in orderbook1.order_dict:
        raise Exception("orderbook_update_cancel order_dict ", i, " fail")
    if ((i + 1) * 4.53, (i + 1) * 3.88 - 9) in orderbook1.price_volume_dict:
        if i in orderbook1.price_volume_dict[((i + 1) * 4.53, (i + 1) * 3.88 - 9)]:
            raise Exception("orderbook_update_cancel price_volume_dict ", i, " fail")
    if i in orderbook1.bid_list or i in orderbook1.ask_list:
        raise Exception("orderbook_update_cancel bid/ask_list ", i, " fail")


# Test update for order book
# Test place order
# Place 10 order

N = 10
update_list1 = []
for i in range(N):
    update_info[i, 0] = i % 2
    update_info[i, 1] = (i + 1) * 4.53
    update_info[i, 2] = (i + 1) * 3.88 - 9
    update_info[i, 3] = (i + 1) * 3.88 - 9
    update_info[i, 5] = i + 79343 + 10
    update_info[i, 6] = 3
    update_info[i, 7] = i * 554

for i in range(update_info.shape[0]):
    update_list1.append(Update(update_info[i, :]))

for i in range(len(update_list1)):
    orderbook1.execute_update(update_list1[i])
    if (30 + i) not in orderbook1.order_dict:
        raise Exception("orderbook_update_place order_dict ", i, " fail")
    if ((i + 1) * 4.53, (i + 1) * 3.88 - 9) not in orderbook1.price_volume_dict:
        raise Exception("orderbook_update_place price_volume_dict ", i, " fail")
    else:
        if (30 + i) not in orderbook1.price_volume_dict[((i + 1) * 4.53, (i + 1) * 3.88 - 9)]:
            raise Exception("orderbook_update_place price_volume_dict ", i, " fail")
    if (i % 2) == 1 and ((30+i) not in orderbook1.bid_list):
        raise Exception("orderbook_update_place bid_list ", i, " fail")
    if (i % 2) == 0 and ((30 + i) not in orderbook1.ask_list):
        raise Exception("orderbook_update_place ask_list ", i, " fail")

# Test update for order book
# Test transact order (partial)
# transact No. 10 - 19 order

update_list2 = []
for i in range(N):
    update_info[i, 0] = (i + 10) % 2
    update_info[i, 1] = (i + 11) * 4.53
    update_info[i, 2] = ((i + 11) * 3.88 - 9) / 2
    update_info[i, 3] = -((i + 11) * 3.88 - 9) / 2
    update_info[i, 5] = i + 20 + 79343
    update_info[i, 6] = 2
    update_info[i, 7] = i * 554 + 1

for i in range(update_info.shape[0]):
    update_list2.append(Update(update_info[i, :]))

for i in range(len(update_list2)):
    orderbook1.execute_update(update_list2[i])
    if ((i + 1) * 4.53, (i + 1) * 3.88 - 9) in orderbook1.price_volume_dict:
        raise Exception("orderbook_update_transact price_volume_dict ", i, " fail")
    if ((i + 1) * 4.53, ((i + 1) * 3.88 - 9)/2) not in orderbook1.price_volume_dict:
        raise Exception("orderbook_update_transact price_volume_dict ", i, " fail")

# Test update for order book
# Test transact order (fully transacted)
# transact No. 10 - 19 order

update_list2 = []
for i in range(N):
    update_info[i, 0] = (i + 20) % 2
    update_info[i, 1] = (i + 21) * 4.53
    update_info[i, 2] = 0
    update_info[i, 3] = -((i + 21) * 3.88 - 9)
    update_info[i, 5] = i + 30 + 79343
    update_info[i, 6] = 2
    update_info[i, 7] = i * 554 + 1

for i in range(update_info.shape[0]):
    update_list2.append(Update(update_info[i, :]))

for i in range(len(update_list2)):
    orderbook1.execute_update(update_list2[i])
    if ((i + 1) * 4.53, (i + 1) * 3.88 - 9) in orderbook1.price_volume_dict:
        raise Exception("orderbook_update_transact price_volume_dict ", i, " fail")
    if (i + 20) in orderbook1.order_dict:
        raise Exception("orderbook_update_transact order_dict ", i, " fail")
    if i in orderbook1.bid_list or i in orderbook1.ask_list:
        raise Exception("orderbook_update_transact bid/ask_list ", i, " fail")



