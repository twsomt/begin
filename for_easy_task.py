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
