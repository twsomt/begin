def t():
    print('true')
    return True

def f():
    print('false')
    return False

if t() and f():
    print('t and f')

if f() and t():
    print('f and t')

if t() or f():
    print('t or f')

if f() or t():
    print('f or t')