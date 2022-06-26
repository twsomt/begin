class Constructor:

    def add_atribute(self, *args):
        setattr(self, args[0], args[1])

    def display(self):
        print(self.__dict__)

obj1 = Constructor()
obj1.display() # печатает {}
obj1.add_atribute('color', 'red')
obj1.add_atribute('width', 20)
obj1.display() # печатает {'color': 'red', 'width': 20}

obj2 = Constructor()
obj2.display() # печатает {}
obj2.add_atribute('height', 100)
obj2.display() # печатает {'height': 100}