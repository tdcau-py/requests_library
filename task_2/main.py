import requests
import os


class YaUploader:
    URL_UPLOAD = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        file_name = file_path.split('\\')[-1]
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}

        params = {'path': f'/{file_name}',
                  'overwrite': 'true', }

        response = requests.get(self.URL_UPLOAD, params=params, headers=headers)
        url_load = response.json().get('href')
        files = {'file': open(file_path, 'rb')}

        resp = requests.put(url_load, params=params, files=files)

        return resp.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.join(os.path.expanduser('~'), 'Desktop\\my_file.txt')
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
