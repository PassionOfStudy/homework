## [숙제 - 달달한 맛 🍫]  지니뮤직의 1~50위 곡의 정보를 스크래핑 (30분 예상) ##
import requests
from bs4 import BeautifulSoup

# 지니뮤직의 1~50위 곡의 정보 사이트 url
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 아래 빈 칸('')을 채워보세요
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)

## Selectors ##
# rank의 Selector
# -> #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# title의 Selector
# -> #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# artist의 Selector
# -> #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis