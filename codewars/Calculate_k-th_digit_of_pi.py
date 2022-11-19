n=10**10010
a=p=2*n
i=1
while a:
    a = a*i // (2*i+1)
    p += a
    i += 1

p = str(p)

def pi(k):
    return int(p[k])