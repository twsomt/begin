from random import randint
x = randint(1, 100)
def is_valid(x):
    return str(x).isdigit() and 1 <= x <= 100

print('Добро пожаловать в числовую угадайку!')
print('Загадано число от 1 до 100.Попробуйте угадать!')
game = 'да'
while game.lower() == 'да':
    counter = 0
    answer = 0
    while not x == answer:
        answer = int(input('Введите целое число: '))
        if not is_valid(answer):
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if answer > x and answer != 0:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif answer < x and answer != 0:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        counter += 1
        print()
    print('Вы угадали, поздравляем!')
    print(f'Вы использовали {counter} попыток')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    game = input('Псс ... сгенерировать новое число?')
