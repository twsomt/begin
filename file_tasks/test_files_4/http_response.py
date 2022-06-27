from requests import get
with open('dataset_3378_2.txt') as file:
    for line in file:
        url = line.strip()
        x = get(url)
        print(len(x.text.strip().splitlines()))