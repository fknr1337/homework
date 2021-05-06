import requests
from pprint import pprint

SIZES = "smxopqryzw"

def most_biggest_size(sizes):
    return max(sizes, key=lambda s: SIZES.index(s['type']))

def get_request():
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
    likes_count = []
    for keys in get_request():
        likes = keys['likes']['count']
        likes_count.append(likes)
        biggest_size = most_biggest_size(keys['sizes'])
        perfect_urls = biggest_size['url']
        urls_list.append(perfect_urls)
    return urls_list


class YandexDisk:

    def __init__(self, token):
        self.token = token


    def upload_by_link(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'url': [i for i in get_urls_list()],
                  'path': ''
                  }
        response = requests.post(url=url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


ya = YandexDisk(token="")

ya.upload_by_link()

