n, k = 5, 2
x = list(range(1, n + 1))
i = 0

print(x)
while len(x) != 1:
    for i in range(0, k-1):
        x.append(x[i])
    del x[0:k]

print(*x)