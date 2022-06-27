x = []
res = {}

with open('dataset_3363_3.txt') as file:
    for line in file:
        line = line.lower().strip()
        x += line.split()

y = set(x)

for i in y:
    res[i] = x.count(i)

for key, value in res.items():
    if value == max(res.values()):
        print(key, value)