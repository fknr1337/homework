import requests
from pprint import pprint

SIZES = "smxopqryzw"

def most_biggest_size(sizes):
    return max(sizes, key=lambda s: SIZES.index(s['type']))

def get_request():
    # token = 'faf2c1a36018142e3564e657e4d5053ed21073db5de508b7be23aa0ae3d412e6c76b462cf25f2adaa136a'
    token = str(input('Введите токе для API VK: '))
    url = 'https://api.vk.com/method/photos.get'
    params = {
            "access_token": token,
            "v": "5.77",
            "album_id": "profile",
            "extended": '1',
            "photo_sizes": '1',
            "owner_id": str(input('Введите id пользователя в VK: ')),
           }
    response = requests.get(url, params=params)
    return response.json()["response"]["items"]

def get_urls_list():
    urls_list = []
    for keys in get_request():
        likes_count = keys['likes']['count']
        biggest_size = most_biggest_size(keys['sizes'])
        perfect_urls = biggest_size['url']
        urls_list.append(perfect_urls)
    return urls_list

def get_likes_count

pprint(get_urls_list())



