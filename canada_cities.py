import json

with open('city.list.json', encoding='utf8') as f:  # opens the city list in json format from api
    data = json.load(f)

# All Ontario cities (That we could find)
ontario = ['Ajax', 'Barrie', 'Belleville', 'Brampton', 'Brant', 'Brantford', 'Brockville', 'Burlington','Cambridge',
           'Clarence-Rockland', 'Cornwall', 'Dryden', 'Delhi', 'Elliot Lake', 'Georgetown','Greater Sudbury', 'Guelph', 'Haldimand County',
           'Hamilton', 'Kawartha Lakes', 'Kenora', 'Kingston', 'Kitchener', 'London', 'Markham', 'Milton', 'Mississauga', 'Newcastle',
           'Niagara Falls', 'Norfolk County', 'North Bay', 'Oakville','Orillia', 'Oshawa', 'Ottawa', 'Owen Sound', 'Paris', 'Parry Sound','Pembroke',
           'Peterborough', 'Pickering', 'Port Colborne', 'Prince Edward County', 'Quinte West', 'Richmond Hill',
           'Sarnia', 'Sault Ste. Marie', 'St. Catharines', 'St. Thomas', 'Stratford', 'Greater Sudbury','Temiskaming Shores', 'Thorold',
           'Thunder Bay', 'Timmins', 'Tottenham','Toronto', 'Vaughan','Waterloo', 'Welland', 'Whitby','Windsor', 'Woodbridge','Woodstock']

canada = []
for city in data:
    if city['country'] == 'CA':  # filters cities to Canada only
        if city['name'] in ontario:  # filters cities to Ontario only
            canada.append(city)  # appends city data (lat, lon, etc.)