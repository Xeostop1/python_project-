import requests
from bs4 import BeautifulSoup
import re
import json

user_agent = {    
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

# url = "https://n.news.naver.com/mnews/ranking/article/023/0003766899?ntype=RANKING&sid=001"
# like_url="https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B76070(period)%5D%7CNEWS%5Bne_023_0003766899%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1685533009909"

#======반응형 데이터 가져오기 json이
#respose json 형태 네트워크에서 찾아보기 →헤더에서 url 가져오기 → 감싸져 있는 함수 띄어내기(callback 부터jQuery33103573876396249236)

url2="https://n.news.naver.com/mnews/article/021/0002574833?sid=100"
articl_url="https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B74127(period)%5D%7CNEWS%5Bne_021_0002574833%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1685536178599"
#기사들 마다 패턴이 url 패턴이 존재 (이기사는 021_0002574833 이게 url에서 패턴을 찾을 수 있음 )
#실제 url을 보면 여기는 sid가 패턴달라짐 내가 가져온 것은 랭킹페이지라서 패턴이 어렵고
#https://n.news.naver.com/mnews/ranking/article/023/0003766899?ntype=RANKING&sid=001
# 아래의 페이지는 oid랑 aid 숫자 움직이면 다른 기사 이동 가능 
#https://entertain.naver.com/read?oid=015&aid=0003840780
# https://n.news.naver.com/mnews/article/021/0002574833?sid=100

#정규표현식 이용 일치하는 곳 다시 보고 정규표현식 하기 → 이건 나중에 크롤링으로 변경 나는 필요한게 이게 아니니까! 
print(re.search("(?<=article)[0-9]+",url2))

res = requests.get(url2, headers=user_agent)
res2 = requests.get(articl_url, headers=user_agent)
soup = BeautifulSoup(res.text, "html.parser")


# 댓글이랑 좋아요 가져와야 되서 딕셔너리 형태로 세팅
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
        },
    "commnets":[]
    
}
# 1차적으로 값있는거 확인 후 → for루프로 값 한개 씩 추출
# 여기서 바로 new딕셔너리에 넣기
for i in res2.json()["contents"][1]["reactions"]:
     news["reaction"][i["reactionType"]]=i["count"]


#=====댓글=======
#접근 불가라서 헤더 추가 wow 그러면 가지고올 수 있따!
headers={
    "Accept":"*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language":
        "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,el;q=0.6,nl;q=0.5,no;q=0.4,da;q=0.3,de;q=0.2,la;q=0.1,ru;q=0.1,ms;q=0.1,mn;q=0.1,my;q=0.1,vi;q=0.1,sv;q=0.1,es;q=0.1,ar;q=0.1,eo;q=0.1,it;q=0.1,zh;q=0.1,th;q=0.1,pt;q=0.1,fr;q=0.1,pl;q=0.1,fi;q=0.1,he;q=0.1",
    "Cookie":
        "NNB=7KBWESYAMU6WI; nx_ssl=2; page_uid=icNwPlprvhGsservdPwssssssTZ-132856",
    "Referer": "https://n.news.naver.com/mnews/article/comment/021/0002574833?sid=100",
    "Sec-Ch-Ua":
        'Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24", "Sec-Ch-Ua-Mobile:?0',
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":    "script",
    "Sec-Fetch-Mode":    "no-cors",
    "Sec-Fetch-Site":    "same-site",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

}
#삭제된 부분 _callback=jQuery331030446041703860693_1685577332131&
#이번에는 그래도 붙어 있는게 있어서 replace로 띄어주기 


commnet_url="https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_politics_m2&pool=cbox5&_cv=20230523152013&lang=ko&country=KR&objectId=news021%2C0002574833&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=1&initialize=true&followSize=5&userType=&useAltSort=true&replyPageSize=20&sort=new&includeAllStatus=true&_=1685577332133"
commnet=requests.get(commnet_url,headers=headers)
#끝에 있는 괄호 제거하기 위해 [:-1]사용

#앞에 콜백문자 제거하고 제이슨형태로 로드로 확인함 
#리플레이스한 뒤쪽에서 json 키값으로 찾기 → 이상태로 바로 for문 돌리기 

last_page=json.loads(commnet.text.replace("_callback(","")[:-2])["result"]["pageModel"]["lastPage"]
print("==========")
#페이지가 0부터 시작해서 len 으로 쓰면 안되나?? 이렇게 하면 1부터 내가 원하는 페이지까지 추출가능(range는 -1까지 만들어짐)
#위쪽 딕셔너리에 "commnet":[] 먼저 넣고 아래쪽에서 리스트로 어펜드

    
for i in range(1, last_page+1):
    commnet_url=f"https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_politics_m2&pool=cbox5&_cv=20230523152013&lang=ko&country=KR&objectId=news021%2C0002574833&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={i}&initialize=true&followSize=5&userType=&useAltSort=true&replyPageSize=20&sort=new&includeAllStatus=true&_=1685577332133"
    for i in json.loads(commnet.text.replace("_callback(","")[:-2])["result"]["commentList"]:
        #순서 딕셔너리[키값].어팬드(들어갈 내용)
        news["commnets"].append(i["contents"].strip())
    
    
#딕셔너리로 만들고 최종으로 json으로 가공하기 (csv 처럼 최종json 형태로 만들기)→ 한글이라 json에 유니코드로 들어갔음 ㅠㅠ
with open("new.json","w",encoding="utf8") as json_file:
    json.dump(news, json_file,ensure_ascii=False)







