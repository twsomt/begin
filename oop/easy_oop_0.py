class Robot:
    def set_name(self, name):
        self.name = name
    
    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')

class Counter:
    def start_from(self, cnt=0):
        self.cnt = cnt
    
    def increment(self):
        self.cnt += 1

    def reset(self):
        self.cnt = 0

    def display(self):
        print(f'Текущее значение счетчика = {self.cnt}')


c1 = Counter()
c1.start_from()
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display() # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"