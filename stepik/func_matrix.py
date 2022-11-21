#print(matrix())        # матрица 1 × 1 из 0
#print(matrix(3))       # матрица 3 × 3 из 0
#print(matrix(2, 5))    # матрица 2 × 5 из 0
#print(matrix(3, 4, 9)) # матрица 3 × 4 из 9

def matrix(n=None, m=None, value=0):
    if n and not m:
        m = n

    if not n:
        n = 1
    
    if not m:
        m = 1

    result = [[value for j in range(m)] for i in range(n)]
    return result

print(matrix(5, 6))
