# def dbl_linear(n):
#     u = [1]
#     x = y = 0
#     while len(set(u)) <= n:
#         a = 2*u[x] + 1 
#         b = 3*u[y] + 1

#         if a > b : 
#             u.append(b)
#             y+= 1 
#         elif a<b : 
#             u.append(a)
#             x += 1 
#         else : 
#             u.append(a)
#             x += 1 
#             y += 1
#     return sorted(set(u))[:n]



# print(dbl_linear(50))


# u = [1,     3, 4,      7, 9, 10, 13,       15, 19, 21, 22         , 27, ...]
# y = 2 * x + 1 and z = 3 * x + 1
# 1 gives 3 and 4,      then 3 gives 7 and 10,    4 gives 9 and 13,     then 7 gives 15 and 22  and so on...


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
            
    return u[:n]

print(dbl_linear(50))