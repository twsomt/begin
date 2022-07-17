from random import shuffle
from os import system
from time import sleep

choice = input('Перемешивать переводы? Enter - да, любое другое значение - нет.')

with open('words.txt', encoding='UTF-8') as file:
    phrases_words = {}
    temp = []
    for line in file:
        x = line.strip()
        if x and not x.isnumeric():
            temp.append(x)
            
            if len(temp) == 2:
                if choice == '':
                    phrases_words[temp[1]] = temp[0]

                phrases_words[temp[0]] = temp[1]
                temp = []

loop = 1
keys = list(phrases_words)

if choice == '':
    cnt_words = int(len(keys) / 2)
else:
    cnt_words = len(keys)
    
while True:
    shuffle(keys)

    for key in keys:
        system('CLS') 
        print(f'Круг номер: {loop}. Слов разучивается: {cnt_words} ')
        print(key)
        x = input('')

        if x == ' ':
            raise SystemExit
        elif x.isnumeric():
            print(phrases_words[key])
            sleep(int(x))
        else:
            print(phrases_words[key])
            sleep(2)

    loop += 1