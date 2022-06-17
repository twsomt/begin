with open('lines.txt', encoding='utf-8') as file:
    lines = file.readlines()
    result = [i.strip() for i in lines if len(i) == max([len(i) for i in lines])]
    
    for line in result:
        print(line)