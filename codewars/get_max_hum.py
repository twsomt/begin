def some_num(n, k):
    n = list(map(int, str(n)))
    l = len(n) - k
    x, y, res = n[:l], n[l:], [] 
    
    while len(x) >= l:
        res.append(max(x))
        pos_elem = x.index(max(x))
        del x[:pos_elem + 1]
        x += y[:pos_elem + 1]
        del y[:pos_elem + 1]
    else:
        res += x
        
    return int(''.join(map(str, res)))

print(some_num(53342, 2))  # 542
print(some_num(102087607280291102, 11))  # 8891102
