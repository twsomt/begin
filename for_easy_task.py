# x = 'Кошка'
# def false_translate(x):
#     return x[::-1].capitalize()

# print(false_translate(x))

# set1 = {'Yellow', 'Orange', 'Black'}
# set2 = {'Orange', 'Blue', 'Pink'}

# set1.difference_update(set2)
# print(*set1)

# x = {'a', 'b'}
# print(x * 2)

# invisible commit

capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

for key, value in sorted(capitals.items(), key = lambda x: x[1]):
    #print(value)
    pass

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011'},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

# names = [i['name'] for i in users if i['phone'][-1] == '8']
# print(*sorted(names))

names = [i['name'] for i in users if i.get("email") == '' or i.get("email") == None]
#print(*sorted(names))

symbols = {
    '1': '.,?!:',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': ' '
}

# 4433555555666110966677755531111
text = 'Hello, World!'

for symbol in text:
    for k, v in symbols.items():
        if symbol.capitalize() in v:
            print(k * (v.index(symbol.capitalize()) + 1), end='')


