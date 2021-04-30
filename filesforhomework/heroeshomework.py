import requests

token = '2619421814940190'

def find_id_hero(name):
    url = (f'https://superheroapi.com/api/{token}/search/{name}')
    res = requests.get(url)
    a = res.json()
    for i in a['results']:
        if name in i.values():
            return(i['id'])


def find_int_hulk(url):
    res = requests.get(url)
    a = res.json()
    return(int(a['intelligence']))

def find_int_captain(url):
    res = requests.get(url)
    a = res.json()
    return(int(a['intelligence']))

def find_int_thanos(url):
    res = requests.get(url)
    a = res.json()
    return(int(a['intelligence']))

hulk_id = find_id_hero('Hulk')
captain_id = find_id_hero('Captain America')
thanos_id = find_id_hero('Thanos')

res_dict = {}
res_dict['Hulk'] = find_int_hulk(f'https://superheroapi.com/api/2619421814940190/{hulk_id}/powerstats')
res_dict['Captain America'] = find_int_captain\
    (f'https://superheroapi.com/api/2619421814940190/{captain_id}/powerstats')
res_dict['Thanos'] = find_int_thanos(f'https://superheroapi.com/api/2619421814940190/{thanos_id}/powerstats')

# Узнаем у какого героя (злодея) больший интеллект
print(max(res_dict, key=res_dict.get))