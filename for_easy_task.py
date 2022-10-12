
for x in range(1000, 1101):
    x = str(x)
    x1 = int(x[0]) + int(x[1])
    x2 = int(x[1]) + int(x[2])
    x3 = int(x[2]) + int(x[3])
    x7 = ''.join(map(str, sorted([min(x1, x2, x3), ((x1 + x2 + x3) - max(x1, x2, x3) - min(x1, x2, x3))], reverse=True)))
    print(f'Запрос: {x} | Ответ: {x7}')