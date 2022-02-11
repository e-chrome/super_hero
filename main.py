import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']
max_intelligence = 0
name_of_hero = ''

for hero in hero_list:
    url = 'https://superheroapi.com/api/2619421814940190/search/' + hero
    response = requests.get(url)
    intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    print(hero, 'intelligence =', intelligence)
    if intelligence > max_intelligence:
        max_intelligence = intelligence
        name_of_hero = hero

print('Результат поиска самого умного героя:')
print(name_of_hero)
