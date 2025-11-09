import requests

url = "https://raw.githubusercontent.com/ipatokal/openflights/master/data/airports.dat"
response = requests.get(url)

with open('airports.dat', 'wb') as f:
    f.write(response.content)

print("Файл airports.dat скачан.")