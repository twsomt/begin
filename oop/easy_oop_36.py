class Cart:
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return list(map(lambda x: f'{x.name}: {x.price}',self.goods))

class Initiliaze:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Table(Initiliaze):
    pass

class TV(Initiliaze):
    pass

class Notebook(Initiliaze):
    pass

class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

cart.add(TV('Philips37', 20000))
cart.add(TV('Philips50', 40000))
cart.add(Table('table_for_laptop', 8000))
cart.add(Notebook('msi', 80000))
cart.add(Notebook('apple', 120000))
cart.add(Cup('blue0.5', 500))



print(cart.get_list())