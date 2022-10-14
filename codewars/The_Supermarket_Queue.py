def queue_time(customers, n):
    if n:
        if n == 1:
            return sum(customers)
        else:
            data = dict()
            counter = 0
            for i in range(1, n + 1):
                data[i] = 0

            data[1] = customers[0]
            iter_cust = 1
            while True:
                if counter == sum(customers):
                    break
                else:
                    pass
                    # todo
            print(data)
    else:
        return 0


print(queue_time([5,3,4], 1))  # 12
print(queue_time([10,2,3,3], 2))  # 10
print(queue_time([2,3,10], 2))  # 12