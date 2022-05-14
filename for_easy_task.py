# x = [[1, 5], [3, 4], [2, 0]]
# print(any(2 in i for i in x))

# # x = 'Кошка'
# # def false_translate(x):
# #     return x[::-1].capitalize()

# # print(false_translate(x))

# # set1 = {'Yellow', 'Orange', 'Black'}
# # set2 = {'Orange', 'Blue', 'Pink'}

# # set1.difference_update(set2)
# # print(*set1)

# # x = {'a', 'b'}
# # print(x * 2)

# # invisible commit

# capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     #print(value)
#     pass

# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011'},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# # names = [i['name'] for i in users if i['phone'][-1] == '8']
# # print(*sorted(names))

# names = [i['name'] for i in users if i.get("email") == '' or i.get("email") == None]
# #print(*sorted(names))

# symbols = {
#     '1': '.,?!:',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
#     '0': ' '
# }

# # 4433555555666110966677755531111
# text = 'Hello, World!'

# for symbol in text:
#     for k, v in symbols.items():
#         if symbol.capitalize() in v:
#             print(k * (v.index(symbol.capitalize()) + 1), end='')

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# keys = set(dict1.keys()) | set(dict2.keys())
# for i in keys:
#     if dict1.get(i) and dict2.get(i):
#         result[i] = dict1[i] + dict2[i]
#     elif dict1.get(i):
#         result[i] = dict1[i]
#     elif dict2.get(i):
#         result[i] = dict2[i]

# print(result)

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

# result = {i: text.count(i) for i in set(text)}


# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

# count_words = {i: s.count(i) for i in s.split()}
# result = []
# for key, value in count_words.items():
#     if value == max(count_words.values()):
#         result.append(key)
# print(min(result))

# x = ('Hatiko', 'Parker', 'Wilson', 50)
# #print(x[1:])


pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for i in pets:
    if i[1:] in result.keys():
        result[i[1:]].append(i[0])
    else:
        result[i[1:]] = [i[0]]

print(result)
