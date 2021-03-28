import json

with open('city.list.json', encoding='utf8') as f:
    data = json.load(f)

canada = []
for city in data:
    if city['country'] == 'CA':
        canada.append(city)