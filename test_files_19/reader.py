with open('population.txt') as file:
    lines = file.readlines()

countries = {' '.join(i.split()[:-1]):i.split()[-1] for i in lines}
for key, value in countries.items():
    if key[0] == 'G' and int(value) > 500000:
        print(f'{key}')