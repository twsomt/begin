def dbl_linear(n) : 
    u = [1] 
    x = y = 0
    while(len(u)<=n) : 
        a = 2 * u[x] + 1 
        b = 3 * u[y] + 1 
        u.append(min(a, b))
        if a < b : x += 1
        elif a > b : y+= 1
        else: 
            x += 1 
            y += 1  
    return u[n]