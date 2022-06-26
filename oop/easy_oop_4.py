class Laptop:
    def __init__(self, brand, model,  price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'

laptop1 = Laptop('msi', 'ge60f', 50000)
laptop2 = Laptop('msi', 'ge60E', 50000)

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"