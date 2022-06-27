file = open('prices.txt', encoding='UTF-8')
lines = file.readlines()
summ = 0

for line in lines:
    temp = list(map(int, line.strip().split('\t')[1:]))
    summ += temp[0] * temp[1]

print(summ)