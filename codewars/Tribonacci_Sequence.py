def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    
    while not len(signature) == n:
        temp = tuple(signature)
        signature.append(temp[-3] + temp[-2] + temp[-1])
    return signature