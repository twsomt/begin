from decimal import Decimal
x = Decimal(input('Введите 1-е число: '))
y = Decimal(input('Введите 2-е число: '))

if x > y:
    print(f'1-е число больше 2-го на {round((x - y) / y * 100, 2)}%')
else:
    print(f'2-е число больше 1-го на {round((y - x) / x * 100, 2)}%')