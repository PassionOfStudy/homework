# [숙제 - 짭짤한 맛 🍜] - 지니뮤직의 1~50위 곡의 정보를 스크래핑 (처음부터 내 손으로)

# 필요한 모듈 import
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017) # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713'
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


## Selector 구조 파악하기
#제목(title)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#순위(rank)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#가수(artist)
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

#공통 부분 -> #body-content > div.newest-list > div > table > tbody > tr
tables_tr = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#title의 경우 문자열의 양쪽 공백을 없애주는 strip() 메소드 사용
#rank의 경우 앞의 두글자가 rank점수이므로 text[0:2] 0번째부터 2보다작은 1번째까지 2개의 글자까지만 선택
music_lists = []
for tr in tables_tr:
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    rank = tr.select_one('td.number').text[0:2].strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    dict = {'title': title, 'rank': rank, 'artist': artist}
    music_lists.append(dict)

#MongoDB 데이터 저장
db.music.insert_many(music_lists)

#MongoDB에 저장된 모든 데이터 조회
print(list(db.music.find({})))
