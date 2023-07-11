import requests


class YaUploader:
    def __init__(self, token: str):
       self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": "/file.docx}", "overwrite": "true"}
        headers = {"Authorization": "OAuth {}".format(self.token)}
        response = requests.get(url, headers=headers, params=params).json()
        url = response.get("href", "")
        with open("C:\\Users\\М.видео\\OneDrive\\Рабочий стол\\file.docx") as f:
            requests.put(url, files={"file": f}, headers=headers, params=params)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\Users\\М.видео\\OneDrive\\Рабочий стол\\file.doc"
    token =""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
