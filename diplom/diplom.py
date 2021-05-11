import requests
from pprint import pprint
from tqdm import tqdm
import json


class VK:

    def __init__(self, vk_id, vk_token):
        self.vk_id = vk_id
        self.vk_token = vk_token


    def get_request(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {
                "access_token": self.vk_token,
                "v": "5.77",
                "album_id": "profile",
                "extended": '1',
                "photo_sizes": '1',
                "owner_id": self.vk_id,
                'count': '5'
               }
        response = requests.get(url, params=params)
        return response.json()["response"]["items"]

    def find_max_res(self, pics, size = 'z'):
        pics = [photo['sizes'] for photo in pics]
        size_photo = []
        for photo in pics:
            for sizes in photo:
                if sizes['type'] == size:
                    size_photo.append({'size': sizes['type'], 'url': sizes['url']})
        return size_photo

    def get_photo_name(self, pics):
        likes_and_dates = [{'likes': photo['likes']['count'], 'date': photo['date']} for photo in pics]
        file_names = []
        for i in likes_and_dates:
             name = str(i['likes']) + '.jpg'
             if name in file_names:
                name = str(i['date']) + name
             file_names.append(name)
        return file_names



class YandexDisk:

    def __init__(self, token):
        self.token = token

    def create_folder(self, folder_name = 'photos'):
        params = {'path': folder_name}
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)
                   }
        r = requests.put(url, headers=headers, params=params)
        return folder_name


    def upload_by_link(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        folder_name = self.create_folder()
        names = vk.get_photo_name(vk.get_request())
        photos = vk.find_max_res(vk.get_request())
        photo_url = [photo['url'] for photo in photos]
        photo_size = [photo['size'] for photo in photos]
        log = []
        for photo, size, names in tqdm(list(zip(photo_url, photo_size, names))):
            params = {'path': f'/{folder_name}/{names}', 'url': photo}
            response = requests.post(url=url, headers=headers, params=params)
            response.raise_for_status()
            log.append({"file_name": names, "size": size})
            if response.status_code == 201:
                 print("Success")
        result = self.create_log_file(log)
        return result

    def create_log_file(self, log):
       with open('log.json', 'w') as file:
           json.dump(log, file)
       return log
            

ya = YandexDisk(token=str(input('Введите токен для Api YandeskDisk: ')))
vk = VK(vk_id=str(input('Введите id пользователя в VK: ')),
        vk_token=str(input('Введите токен для API VK: ')))
ya.upload_by_link()
