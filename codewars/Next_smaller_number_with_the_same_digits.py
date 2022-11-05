def relocater(x, y, z):
    h = list(x)
    h[y], h[z] = x[z], x[y]
    h = sorted(h[:y]) + h[y:]
    return ''.join(h)

def next_smaller(n):
    n = str(n)
    if list(n) == sorted(n):
        return -1
    m = n[::-1]
    for i, k in enumerate(m,0):
        if any(x for x in m[:i] if x < k):
            _, j = max(((x, j) for j, x in enumerate(m[:i]) if int(x) < int(k)),key = lambda x:(x[0], x[1]))
            y = relocater(m, i, j)
            if not y.endswith('0'):
                return int(y[::-1])
    return -1

array = (907, 531, 135, 2071, 414, 123456798, 123456789, 1234567908, )

for t in array:
    print(f'{t} * {next_smaller(t)}')

# (907), 790)
# (531), 513)
# (135), -1)
# (2071), 2017)
# (414), 144)
# (123456798), 123456789)
# (123456789), -1)
# (1234567908), 1234567890)