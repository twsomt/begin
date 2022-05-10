mat, fiz, rus, cnt = 0, 0, 0, 0
with open('dataset_3363_4.txt') as file:
    for line in file:
        temp = list(map(float, line.split(';')[1:]))
        mat += temp[0]
        fiz += temp[1]
        rus += temp[2]
        cnt += 1
        print(sum(temp) / len(temp))

    print(mat / cnt, fiz / cnt, rus / cnt)
    