from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv
import codecs
import requests
import json

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--lang=ko-KR")
options.add_argument("lang=ko")
options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko_KR"})
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()



#=====펫프렌즈 상품 리뷰스크래핑====



loading=5
max_h=5000

headers={
"Accept":*/*
Accept-Encoding:
gzip, deflate, br
Accept-Language:
ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,el;q=0.6,nl;q=0.5,no;q=0.4,da;q=0.3,de;q=0.2,la;q=0.1,ru;q=0.1,ms;q=0.1,mn;q=0.1,my;q=0.1,vi;q=0.1,sv;q=0.1,es;q=0.1,ar;q=0.1,eo;q=0.1,it;q=0.1,zh;q=0.1,th;q=0.1,pt;q=0.1,fr;q=0.1,pl;q=0.1,fi;q=0.1,he;q=0.1
Content-Length:
410
Content-Type:
application/json
Origin:
https://m.pet-friends.co.kr
Referer:
https://m.pet-friends.co.kr/
Sec-Ch-Ua:
"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Sec-Ch-Ua-Mobile:
?0
Sec-Ch-Ua-Platform:
"Windows"
Sec-Fetch-Dest:
empty
Sec-Fetch-Mode:
cors
Sec-Fetch-Site:
same-site
User-Agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
}
# url="https://m.pet-friends.co.kr/category/2/4/19?route_detail=ct_home&filters=orderBy%5C-product_score"
url="https://mobile.api.pet-friends.co.kr/essearch/category/product/list"
asyn_page=requests.get(url,headers=headers)
browser.get(url, )
time.sleep(loading)
# ["dehydratedState"]["queries"]["state"]["data"]
item_json=asyn_page.json()["pageProps"]["dehydratedState"]["queries"]

for i in item_json:
    for j in i["state"]:
        print(j)
    
        
        
    

#=====스크롤 다운=======
def scroll_down():
    #바로 들어와서 바로 보이는 첫번째 높이 가져오기 
    old_h=browser.execute_script("return document.documentElement.scrollHeight")
    num=0
    
    while True:
        num+=1
        print("이전 웹 문서 높이", old_h)
        print(f"스크롤 아래로 {num}회차 ")
        #문서높이 만큼 
        cur_h="document.documentElement.scrollHeight"
        
        browser.execute_script(f"window.scrollTo(0,{cur_h})")
        print("최하단")
        time.sleep(loading) 
        #툴팁((좋아요 손모양))때문에 이벤트 때문에 깨긋한 화면으로 만든 상태(오류없이 살짝 올려준 상태)
        loading_h=600   
        browser.execute_script(f"window.scrollTo(0,{loading_h})")
        print("상단에서 +600")
        time.sleep(loading)
        new_h=browser.execute_script(f"return {cur_h}")
        
        #새높이
        if new_h==old_h or new_h>=max_h:
            print("=====스크롤 작업완료======")
            break 
        old_h=new_h
        
# scroll_down()





    