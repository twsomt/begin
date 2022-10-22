x = [
('y', 4, 2),
('s', 3, 1),
('c', 3, 1),
('d', 3, 2),
('n', 3, 1),
('z', 2, '='),
('a', 2, '=')]

def foo(tpl):
    if tpl[2] == '=':
        return -tpl[1], 0, tpl[0]
    return -tpl[1], tpl[2], tpl[0]


res = sorted(x, key=foo)
print(*res, sep='\n')