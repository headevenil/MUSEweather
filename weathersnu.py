import requests
#pip3 install beautifulsoup4
#pip3 install lxml
from bs4 import BeautifulSoup

def getWeatherSNU():
    #기상청 동네예보 RSS - 관악구 대학동
    _url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1162073500'
    response = requests.get(_url)
    result = response.content

    soup = BeautifulSoup(result, features="xml")
    data = soup.rss.channel.item.description.body.data.wfEn
    weather = data.string

    #Prints a 3 hour weather prediction for SNU (daehak dong)
    print(weather)


if __name__ == '__main__':
    getWeatherSNU()

'''
http://www.kma.go.kr/images/weather/lifenindustry/timeseries_XML.pdf
^ explains the data

possible weather values:
① Clear
② Partly Cloudy
③ Mostly Cloudy
④ Cloudy
⑤ Rain
⑥ Snow/Rain
⑦ Snow
'''
