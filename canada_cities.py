import json

with open('city.list.json', encoding='utf8') as f:
    data = json.load(f)

ontario = ['Barrie', 'Belleville', 'Brampton', 'Brant', 'Brantford', 'Brockville', 'Burlington', 'Cambridge',
           'Clarence-Rockland', 'Cornwall', 'Dryden', 'Elliot Lake', 'Greater Sudbury', 'Guelph', 'Haldimand County',
           'Hamilton', 'Kawartha Lakes', 'Kenora', 'Kingston', 'Kitchener', 'London', 'Markham', 'Mississauga',
           'Niagara Falls', 'Norfolk County', 'North Bay', 'Orillia', 'Oshawa', 'Ottawa', 'Owen Sound', 'Pembroke',
           'Peterborough', 'Pickering', 'Port Colborne', 'Prince Edward County', 'Quinte West', 'Richmond Hill',
           'Sarnia', 'Sault Ste. Marie', 'St. Catharines', 'St. Thomas', 'Stratford', 'Temiskaming Shores', 'Thorold',
           'Thunder Bay', 'Timmins', 'Toronto', 'Vaughan', 'Waterloo', 'Welland', 'Windsor', 'Woodstock']

canada = []
for city in data:
    if city['country'] == 'CA':
        if city['name'] in ontario:
            canada.append(city)
