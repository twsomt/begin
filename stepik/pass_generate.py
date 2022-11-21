from random import *

chars = ''
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exceptions = ''
qty_password = 0
len_password = 0

questions = [
    'Какое количество паролей сгенерировать? ',
    'Какая длина одного пароля ? ',
    'Включать ли цифры 0123456789 ? ',
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ',
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? ',
    'Включать ли символы !#$%&*+-=?@^_ ? ',
    'Исключать ли неоднозначные символы il1Lo0O ? '
]

for i in range(len(questions)):
    answ = input(questions[i])
    if i == 0:
        qty_password = int(answ)
    elif i == 1:
        len_password = int(answ)
    elif i == 2 and answ == 'да':
        chars += digits
    elif i == 3 and answ == 'да':
        chars += lowercase_letters
    elif i == 4 and answ == 'да':
        chars += uppercase_letters
    elif i == 5 and answ == 'да':
        chars += punctuation
    elif i == 6 and answ == 'да':
        exceptions += ''


def generate(chars, len_password, exceptions):
    result = ''
    while len(result) != len_password:
        symbol = chars[randint(0, len(chars) - 1)]
        if len(exceptions) != 0:
            if not symbol in exceptions:
                result += symbol
        else:
            result += symbol
    return result


print()
for i in range(1, qty_password + 1):
    print(f'Пароль #{i}: {generate(chars, len_password, exceptions)}')

print('Генерация завершена. Возврашайтесь, если понадобятся ещё пароли')
