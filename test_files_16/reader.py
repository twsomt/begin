with open('file.txt', encoding='utf-8') as file:
    # for line in file.readlines():
    #     print(line.strip())
    content = file.read().strip()

    letters = len(list(filter(lambda x: x.isalpha(), content)))
    words = len(content.split())
    lines = content.count('\n') + 1

    print(f'''Input file contains:
{letters} letters 
{words} words 
{lines} lines''')


    
