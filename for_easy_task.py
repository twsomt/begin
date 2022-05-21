# def generate_ip():
#     from random import randint
#     return f'{randint(100, 255)}.{randint(100, 255)}.{randint(0, 9)}.{randint(100, 255)}'

# print(generate_ip())


# from random import shuffle
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]

# [shuffle(i) for i in matrix]


# from random import shuffle 
# word = list(input())
# shuffle(word)
# print(''.join(word))

# from random import randint as r
# temp = set()
# while not len(temp) == 25:
#     temp.add(str(r(1, 75)).ljust(3))

# temp = list(temp)
# temp[12] = '  0'

# for i in range(0, 30, 5):
#     print(*temp[i-5:i])
    


# from random import randint as r
# bingo = [[str(r(1, 75)).ljust(3) for i in range(5)] for j in range(5)]
# bingo[2][2] = ' 0 '
# [print(*i) for i in bingo]


# from re import sub
# from string import ascii_letters, digits
# from random import sample


# x = ascii_letters + digits
# y = sub(r'[lI1oO0]', '', x)
# print(x)
# print(y)

# from fractions import Fraction

# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
# x = min(map(Fraction, s.split()))
# y = max(map(Fraction, s.split()))

# print(x + y)


def func(qty): return {chr(96 + i):i for i in range(1, qty + 1)}
print(func(3))
