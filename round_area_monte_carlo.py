from random import uniform
n = 10**6
k = 0
s0 = 4

for _ in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    print(x, y)

    if x ** 2 + y ** 2 <= 1:
        k += 1

print(k / n * s0)