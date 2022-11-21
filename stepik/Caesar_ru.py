text = 'Я тебя люблю!' # исходный текст
alp = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' # алфавит
shift = 10 # сдвиг

if shift > 0: shift -= 32

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