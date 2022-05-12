classes = {}
with open('dataset_3380_5.txt') as file:
    for line in file:
        x = line.strip().split()
        if not int(x[0]) in classes:
            classes[int(x[0])] = [1, float(x[2])]
        else:
            classes[int(x[0])][0] += 1
            classes[int(x[0])][1] += float(x[2])

for i in range(1,12):
    print(i, end=' ')
    if i in classes:
        print(classes[i][1] / classes[i][0])
    else:
        print('-')

