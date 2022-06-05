# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result


# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result


# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

# print(sum(map(lambda x: x ** 2 ,filter(lambda x: len(str(abs(x))) == 2 and x % 7 == 0 ,numbers))))


# def func(elem1, elem2, elem3, elem4):
#     return elem1 + elem2 + elem3 + elem4


# numbers1 = [1, 2, 3, 4]
# numbers2 = [10, 20, 30]
# numbers3 = [100, 200, 300, 400, 500]
# numbers4 = [100, 200, 300, 400, 500]

# new_numbers = list(map(func, numbers1, numbers2, numbers3, numbers4))  #  преобразуем итератор в список

# print(new_numbers)


# x = 56466464644646
# print(f'{x}')



# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
# result = list(map( lambda x: 'even' if x % 2 == 0 else 'add',numbers))

# print(numbers)
# print(result)

# from functools import reduce

# numbers = range(10)
# obj = map(lambda x: x + 1, numbers)
# obj = filter(lambda x: x % 2 == 1, obj)
# result = reduce(lambda x, y: x + y, obj, 0)

# print(result)


from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]


res = ', '.join(sorted(list((map(lambda x: x[0], (filter(lambda x: x[1] > 10000000 and x[-1] == 'primary', data)))))))
print(f'Cities: {res}')