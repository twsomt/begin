x = [
('y', 4, 2),
('s', 3, 1),
('c', 3, 1),
('d', 3, 2),
('n', 3, 1),
('z', 2, '='),
('a', 2, '=')]

# print(x)
x = sorted(x, key=lambda x: x[1], reverse=True)
# print(x)


x_res = []
n = len(set([i[1] for i in x]))

for _ in range(n):
    temp = []
    y = x[0][1]
    yy = 0
    cnt = 0
    while True:
        yy = y
        try:
            y = x[cnt][1]
        except:
            break
        
        if y != x[0][1]:
            break
        
        temp.append(x[cnt])
        cnt += 1
        
    temp_1 = sorted([i for i in temp if i[-1] != '='], key=lambda x: (x[-1], x[0]))
    temp_2 = sorted([i for i in temp if i[-1] == '='], key=lambda x: (x[-1], x[0]))
    temp = temp_1 + temp_2
    x_res += temp
    
    x = [i for i in x if i[1] != yy]


[print(i) for i in x_res]
