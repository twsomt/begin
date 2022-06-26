class Zebra:
    def __init__(self):
        self.cnt = 0
        self.white = 'Полоска белая'
        self.black = 'Полоска черная'

    def which_stripe(self):
        print(self.white if self.cnt % 2 == 0 else self.black)
        self.cnt += 1

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"