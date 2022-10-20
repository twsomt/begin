def array_diff(a, b):
    if a and b:
        return [i for i in a if all( i != j for j in b)]
    elif a:
        return a
    return []