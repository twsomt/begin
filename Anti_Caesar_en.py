text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.' # исходный текст
alp = 'abcdefghijklmnopqrstuvwxyz' # алфавит
shift = 0 - 25 # 0 минус сдвиг для дешифрования

if shift > 0: shift -= 26

def code(txt, alp):
    result = ''
    for i in text: #для каждого символа в исходном тексте
        if i in alp:
            # добавляем в result значение из alp с индексом найденного в нём символа с учётом сдвига
            result += alp[alp.find(i) + shift]
        elif i.lower() in alp:
            # то же самое но сохраняем регистр
            result += alp[alp.find(i.lower()) + shift].upper()
        else:
            # если буква это вовсе не буква русского алфавита, то просто добавляем её в результат без изменений
            result += i
    return result

print(f'Исходный текст: {text}')
print(f'Зашифрованный текст: {code(text, alp)}')