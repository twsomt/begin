from string import ascii_letters, punctuation
from random import sample
length_pass = int(input('Какойдлины пароль сгенерировать?'))
print(''.join(sample(ascii_letters + punctuation, length_pass)))