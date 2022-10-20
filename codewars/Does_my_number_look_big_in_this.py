def narcissistic(v):
    return v == sum([int(i) ** len(str(v) for i in str(v)]) 
