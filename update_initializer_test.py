import numpy as np
from update import *

N = 10
update_info = np.zeros((N, 8))
update_list = []
for i in range(N):
    update_info[i, 0] = i % 2
    update_info[i, 1] = i * 23.23
    update_info[i, 2] = i * 2.33
    update_info[i, 3] = i * 5.49
    update_info[i, 5] = i * 79343
    update_info[i, 6] = (i * 2) % 3 + 1
    update_info[i, 7] = i * 554

for i in range(update_info.shape[0]):
    update_list.append(Update(update_info[i, :]))

for i in range(len(update_list)):
    update = update_list[i]
    if update.is_bid != i % 2 or update.price != i * 23.23 or update.remaining != i * 2.33 or update.delta != i * 5.49 \
            or update.timestamp != i * 79343 or update.reason != (i * 2) % 3 + 1 or update.id != i * 554:
        raise Exception("test_initializer ", i, " fail")

for i in range(len(update_list)):
    update = update_list[i]
    if update.get_is_bid() != (i % 2 == 1) or update.get_price() != i * 23.23 or update.get_remaining() != i * 2.33 or\
            update.get_delta() != i * 5.49 or update.get_timestamp() != i * 79343 or\
            update.get_reason() != (i * 2) % 3 + 1 or update.get_id() != i * 554:
        raise Exception("test_getter ", i, " fail")


