def is_prime(num):
    if n <= 0 or n == 1:
        return False
    i = 2
    while (i <= n ** 0.5 ):
        if n % i == 0:
        return False
        i += 1
    return True

print(is_prime(5))
print(is_prime(6))
print(is_prime(7))