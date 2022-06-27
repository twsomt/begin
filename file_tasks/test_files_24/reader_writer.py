def plus_five(num):
    num = int(num) + 5
    if num > 100:
        return 100
    else:
        return num

with open('class_scores.txt', 'r', encoding='utf-8') as read_file, open('new_scores.txt', 'w', encoding='utf-8') as out_file:
    for klass, score in map(lambda x: x.strip().split() ,read_file.readlines()):
        print(f'{klass} {plus_five(score)}', file=out_file)
