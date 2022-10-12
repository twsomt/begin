def search(budget, prices):
    return ','.join(map(str, sorted(list(filter(lambda x: x <= budget ,prices)))))


print(search(14, [7, 3, 23, 9, 14, 20, 7]))