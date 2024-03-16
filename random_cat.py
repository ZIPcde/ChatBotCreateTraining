import requests

def cat():
    url = 'https://api.thecatapi.com/v1/images/search'  # Замените URL на нужный
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]['url']  # Получение значения от ключа "url" из первого элемента списка

if __name__ == '__main__':
    cat_image_url = cat()
    print(cat_image_url)
