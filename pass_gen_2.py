# принимает на вход длину пароля и оп-оп генерит
from string import ascii_letters, punctuation
from random import sample
from pandas import DataFrame

length_pass = int(input('Какой длины пароль сгенерировать? [Максимум - 84]: '))
password = ''.join(sample(ascii_letters + punctuation, length_pass))

result = DataFrame([password])
result.to_clipboard(index=False,header=False)

print('Пароль скопирован в буфер обмена!')