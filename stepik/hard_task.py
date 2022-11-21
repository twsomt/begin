def create(name, parent):
    if not names.get(parent, False):
        names[parent] = []
    names[parent].append(name)

def add(name, var):
    if not variables.get(name, False):
        variables[name] = []
    variables[name].append(var)

def get(name, var):
    res = None
    temp = variables.get(name, False)
    if not temp or var not in temp:
        for key, value in names.items():
            if name in value:
                res = get(key, var)
    else:
        res = name
    return res

names = {}
variables = {}

n = int(input())

for _ in range(n):
    cmd, place, value = input().split()
    if cmd == 'add':
        add(place, value)
    elif cmd == 'create':
        create(place, value)
    elif cmd == 'get':
        print(get(place, value))