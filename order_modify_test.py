from order import *
import numpy as np
from update import *

N = 10
update_info = np.zeros((N, 8))
order_list = []
for i in range(N):
    update_info[i, 0] = i % 2
    update_info[i, 1] = i * 23.23
    update_info[i, 2] = (i % 3) * 2.33
    update_info[i, 3] = i * 5.49
    update_info[i, 5] = i * 79343
    update_info[i, 6] = i % 2 + 1
    update_info[i, 7] = i * 554

for i in range(update_info.shape[0]):
    order_list.append(Order(Update(update_info[i, :])))

for i in range(len(order_list)):
    order = order_list[i]
    if i % 2 + 1 == 1:
        if order.get_remaining() != 0 or (not order.is_dead) or order.deathtime != i * 79343:
            raise Exception("test_order_modify ", i, " fail")
    if i % 2 + 1 == 2:
        if order.get_remaining() != i * 2.33:
            raise Exception("test_order_modify ", i, " fail")
        if order.get_remaining() == 0:
            if (not order.is_dead) or order.deathtime != i * 79343:
                raise Exception("test_order_modify ", i, " fail")
