import json
json_file = open('/home/twsomt/projects/begin/.idea/web_scrapping/webinars.json', 'r')

json_data = json.load(json_file)
# print(json_data)

for item in json_data:
    print(item['name'])
    print(item['speaker'])
    print('\n')