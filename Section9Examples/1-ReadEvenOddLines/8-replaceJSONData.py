import json

with open('urls.json', 'r') as file:
     data = json.load(file)
     for item in data:
        #item['url'] = item['url'].replace("http", "https")
        item['url'] = item['url'].replace("http:", "https:")

with open('urls.json', 'w') as file:
    json.dump(data, file, indent=2)