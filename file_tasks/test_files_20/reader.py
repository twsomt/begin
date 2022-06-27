def read_csv():
    with open('data.csv') as file:
        lines = file.readlines()
    keywords = lines[0].strip().split(',')
    result = []

    for line in lines[1:]:
        result.append({keywords[i]: line.strip().split(',')[i] for i in range(len(keywords))})

    return result

print(read_csv())