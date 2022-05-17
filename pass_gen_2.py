# принимает на вход длину пароля и оп-оп генерит
from string import ascii_letters, punctuation
from random import sample
length_pass = int(input('Какой длины пароль сгенерировать?'))
print(''.join(sample(ascii_letters + punctuation, length_pass)))
