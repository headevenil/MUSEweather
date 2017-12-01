import requests
#pip3 install beautifulsoup4
#pip3 install lxml
from bs4 import BeautifulSoup
import json
import pprint

#foreign website
def getCoorFromIP():
    _url = 'http://ip-api.com/json/'

    response = requests.get(_url)
    result = response.json()

    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(result)

    _lat = result["lat"]
    _long = result["lon"]

    return (_lat, _long)

#korean website
def getBetterCoorFromIP():
    #http://findip.opendocs.co.kr/exe/process?ip_address=58.143.152.134
    #alternate source of location, but needs the ip from elsewhere

    _url = 'http://mylocation.co.kr/'
    response = requests.get(_url)
    result = response.content

    soup = BeautifulSoup(result, features="xml")
    naver = soup.find_all("a", id="HyperNaver")
    naverURL = naver[0]['href']
    naverList = naverURL.split("&")

    _lat = naverList[1][4:]
    _long = naverList[2][4:]

    return (_lat, _long)


def getWeatherFromCoor(_lat, _long):
    _key = 'fe63de5621d53586399ca58fe30afdaa'
    _url = "http://api.openweathermap.org/data/2.5/weather?lat="
    _url += str(_lat) + "&lon=" + str(_long) + "&units=metric&appid=" + str(_key)

    response = requests.get(_url)
    result = response.json()

    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(result)
    print(result['weather'][0]['description'])

if __name__ == '__main__':
    coor = getBetterCoorFromIP()
    getWeatherFromCoor(*coor)

    #coor = getCoorFromIP()
    #getWeatherFromCoor(*coor)


'''
list of descriptions include:
clear sky
few clouds
scattered clouds
broken clouds
shower rain
rain
thunderstorm
snow
mist
'''
