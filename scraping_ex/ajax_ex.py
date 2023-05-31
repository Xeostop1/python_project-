import requests
from bs4 import BeautifulSoup
import re

user_agent = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# url = "https://n.news.naver.com/mnews/ranking/article/023/0003766899?ntype=RANKING&sid=001"
# like_url="https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B76070(period)%5D%7CNEWS%5Bne_023_0003766899%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1685533009909"



url2="https://n.news.naver.com/mnews/article/021/0002574833?sid=100"
articl_url="https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B74127(period)%5D%7CNEWS%5Bne_021_0002574833%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1685536178599"
#기사들 마다 패턴이 url 패턴이 존재 (이기사는 021_0002574833 이게 url에서 패턴을 찾을 수 있음 )
#실제 url을 보면 여기는 sid가 패턴달라짐 내가 가져온 것은 랭킹페이지라서 패턴이 어렵고
#https://n.news.naver.com/mnews/ranking/article/023/0003766899?ntype=RANKING&sid=001
# 아래의 페이지는 oid랑 aid 숫자 움직이면 다른 기사 이동 가능 
#https://entertain.naver.com/read?oid=015&aid=0003840780
# https://n.news.naver.com/mnews/article/021/0002574833?sid=100

#정규표현식 이용 일치하는 곳 다시 보고 정규표현식 하기 
print(re.search("(?<=article)[0-9]+",url2))

res = requests.get(url2, headers=user_agent)
res2 = requests.get(articl_url, headers=user_agent)
soup = BeautifulSoup(res.text, "html.parser")



# 댓글가져와야 되서 딕셔너리 형태로 세팅
news={
    "title": soup.select_one("h2#title_area > span").text.strip(),
    #이렇게 해도 다 가져 올 수 있네 
    "content":soup.select_one("div#dic_area").text.strip(),
    #딕셔너리 형태로 넣기 
    "reaction": {
        "touched": 0,
        "analytical":0,
        "useful":0,
        "wow":0,
        "recommend":0
        }
    
}
# 1차적으로 값있는거 확인 후 → for루프로 값 한개 씩 추출
# 여기서 바로 new딕셔너리에 넣기
for i in res2.json()["contents"][1]["reactions"]:
     news["reaction"][i["reactionType"]]=i["count"]

#======반응형 데이터 가져오기 json이
#respose json 형태 네트워크에서 찾아보기 →헤더에서 url 가져오기 → 감싸져 있는 함수 띄어내기(callback 부터jQuery33103573876396249236)

# print(news)




