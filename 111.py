import requests

img = 'https://masyamba.ru/%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BB%D1%8C%D0%B2%D0%B0/28-%D0%BB%D0%B5%D0%B2-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8.jpg'

response = requests.get(img)

with open('test.jpg', 'wb') as file:
    file.write(response.content)