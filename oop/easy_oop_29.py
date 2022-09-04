class Translator:
    my_dict = {}
    
    def add(self, eng, rus):
        if eng not in self.my_dict:
            self.my_dict[eng] = [rus]
        elif rus not in self.my_dict[eng]:
            self.my_dict[eng].append(rus)

    def remove(self, eng):
        del self.my_dict[eng]

    
    def translate(self, eng):
        return self.my_dict[eng]

    
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(*tr.translate('go'))