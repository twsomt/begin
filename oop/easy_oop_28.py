import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        if len(self.lst_data) > b:
            return list(self.lst_data[i] for i in range(a, b+1))
        else:
            return list(self.lst_data[i] for i in range(a, len(self.lst_data)))
        
    
    def insert(self, data):
        for j in data:
            self.lst_data.append({k:v for k, v in zip(self.FIELDS, j.split())})
        return self.lst_data

db = DataBase()
db.insert(lst_in)