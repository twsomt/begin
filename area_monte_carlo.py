from random import uniform
n = 10**6
k = 0
s0 = 16

for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)
    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
        k += 1

print(k / n * s0)