from order import *

N = 10
order_info = np.zeros((N, 3))
order_list = []
for i in range(N):
    order_info[i, 0] = (i+1) % 2 + 1
    order_info[i, 1] = (i+1) * 4.53
    order_info[i, 2] = (i+1) * 3.88 - 9

for i in range(order_info.shape[0]):
    order_list.append(Order(order_info[i, :]))

for i in range(len(order_list)):
    order = order_list[i]
    if order.id != i or order.is_bid != ((i+1) % 2 + 1 == 1) or order.price != (i+1) * 4.53 or order.remainming != (i+1) * 3.88 - 9\
            or order.is_dead == True or order.birthtime != 0 or order.deathtime != float('inf'):
        raise Exception("test", i, "fail")

#todo:
#1.test Update initializer
#2.test Order initilializer with an Update object as parameter
#3.test modify method in Order class