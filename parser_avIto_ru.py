from email import header
import requests 
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

url = 'https://www.avito.ru/saransk/avtomobili/bityy-ASgBAgICAUTyCrKKAQ?cd=1&f=ASgBAgECAUTyCrKKAQFFxpoMG3siZnJvbSI6MTUwMDAwLCJ0byI6NTAwMDAwfQ&radius=200'
res = requests.get(url, headers=header)

soup = BeautifulSoup(res.text, 'html.parser')
carDiv = soup.find('div', class_='iva-item-root-_lk9K')

carName = carDiv.find('a', class_='link-link-MbQDP').text
carLink = carDiv.find('a', class_='link-link-MbQDP').get('href')
carSity = carDiv.find('div', class_='geo-georeferences-SEtee').find('span').text
carPrice = carDiv.find('span', class_='price-text-_YGDY').text

allCar = soup.findAll('div', class_='iva-item-root-_lk9K')

allCarData = []
for car in allCar:    
    carName = car.find('a', class_='link-link-MbQDP').text
    carLink = 'https://www.avito.ru' + car.find('a', class_='link-link-MbQDP').get('href')
    carSity = car.find('div', class_='geo-georeferences-SEtee').find('span').text
    carPrice = car.find('span', class_='price-text-_YGDY').text
    priceCar = []
    for car in carPrice:
        if car.isdigit():
            priceCar.append(car)
        else:
            continue 

    allCarData.append([carName, carLink, carSity, *priceCar])
print(allCarData)
#Test

