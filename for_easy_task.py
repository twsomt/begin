import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']

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
print(db.select(0, 1))


matrix = [
    [False, True, False],
    [True, False, False],
    [False, False, True]
]

res = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

for i in range(3):
            for j in range(3):
                if i == 0:
                    if j == 0:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j])))
                    elif j == 3-1:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j])))
                    else:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1], matrix[i][j+1])))
                elif i == 3-1:
                    if j == 0:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1])))
                    elif j == 3-1:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1])))
                    else:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1])))
                else:
                    if j == 0:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j])))
                    elif j == 3-1:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1], matrix[i+1][j-1], matrix[i+1][j])))
                    else:
                        res[i][j] = sum(map(lambda x: 1 if x else 0, (matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j], matrix[i+1][j-1], matrix[i][j-1])))

for i in matrix:
    for j in i:
        print(str(j).ljust(6), end=' ')
    print()

print()

for i in res:
    for j in i:
        print(str(j).ljust(6), end=' ')
    print()