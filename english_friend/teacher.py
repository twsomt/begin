import random 
import os 
import time

os.system('CLS') 

with open('words.txt', encoding='UTF-8') as file:
    phrases_words = {}
    temp = []
    for line in file:
        x = line.strip()
        if x and not x.isnumeric():
            temp.append(x)
            
            if len(temp) == 2:
                phrases_words[temp[0]] = temp[1]
                temp = []

loop = 1

while True:
    keys = list(phrases_words)
    random.shuffle(keys)


    for key in keys:
        print(f'Круг номер: {loop}. Слов разучивается: {len(keys)} ')
        print(key)
        x = input('')

        if x == ' ':
            raise SystemExit
        elif x.isnumeric():
            print(phrases_words[key])
            time.sleep(int(x))
        else:
            print(phrases_words[key])
            time.sleep(2)

        os.system('CLS')
    loop += 1