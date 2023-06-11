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
options.add_argument("--headless")
options.add_argument("--lang=ko-KR")
options.add_argument("lang=ko")
options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko_KR"})
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()



#=====펫프렌즈 상품 리뷰스크래핑====
loading=5
max_h=10000
url="https://m.pet-friends.co.kr/category/2/4/19?route_detail=ct_home&filters=orderBy%5C-product_score"
browser.get(url)
time.sleep(loading)
        
        

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
        
scroll_down()
#=====데이터 추출======
soup=BeautifulSoup(browser.page_source,"html.parser")
item_list=soup.select(".c-dYjrYg.c-dYjrYg-ejCoEP-direction-row.c-dYjrYg-irEjuD-align-stretch.c-dYjrYg-awKDG-justify-start.c-dYjrYg-kVNAnR-wrap-noWrap.c-dYjrYg-iepAfiZ-css")
results=[]
items={}
for i in item_list:
    commnet_num=i.select_one(".c-jKPMbO.c-jKPMbO-fAZBuy-variant-h6.c-jKPMbO-icSlbEp-css").get_text().strip()[1:-1]
    price=i.select_one(".c-jKPMbO.c-jKPMbO-hifKBS-variant-h2.c-jKPMbO-iiuedIb-css").get_text().strip()
    items={
        "name":i.select_one(".c-jKPMbO.c-jKPMbO-jYRJpG-variant-h4.c-jKPMbO-ieBnYpE-css").get_text().strip().replace(",", " "),
        "price":price,
        "commnet_num":commnet_num
    }
    results.append(items)
    
# print(results)

with codecs.open("product_petfri.csv", "wb", encoding="utf-8-sig") as f:
    header = ['name', 'price','commnet_num']
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    for item in results:
        w.writerow(item)


    