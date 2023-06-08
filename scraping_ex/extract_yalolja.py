from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import  BeautifulSoup
import time
import csv
import codecs

#======야놀자 스크래핑=====
#변수: 티켓이름, 가격
#야놀자:셀레니움 스크롤 조작 이용 후 list 형태로 csv저장
# 공모전에 필요한 로우데이터로 사용하기 위해 
# 지역별 티켓판매 현황(티켓이름)과 가격 스크래핑
#=== 향후 업데이트===
#1. 추후 관광 감성어 추출 업데이트가 필요(https://www.yanolja.com/magazine?source=DI_RECOMMEND_MAGAZINE___W42)
#2. try except 처리 필요



#======환경세팅================
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options=webdriver.ChromeOptions()
options.add_argument('--headless')                              
options.add_argument("window-size=1920x1080")      
options.add_argument(f"user-agent={user_agent}")   
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options))
browser.maximize_window()                        

results=[]
items={}
#=======bs4 파싱==============
url="https://www.yanolja.com/leisure/list?mediumcat=10120006"
browser.get(url) 
time.sleep(3)  
#====데이터추출하기======== 


#===========스크롤 내리기===============
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
	#첫번째로 스크롤 내리기
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	#시간대기
	time.sleep(2)
	#현재높이 저장
	current_height = browser.execute_script("return document. body.scrollHeight")
	#현재높이와 끝의 높이가 끝이면 탈출
	if current_height == prev_height:
		break
	#업데이트해줘서 끝낼 수 있도록 
	prev_height = current_height

soup=BeautifulSoup(browser.page_source, "html.parser")
item_list=soup.select("a.LeisureListItem_container__12YuE")

for i in item_list:
    items={
     	"title":i.select_one("p.LeisureListItem_title__U-d8s").get_text().strip().replace(",", " "),
     	"price":i.select_one("span.LeisurePriceDiscount_amount__19qBa").get_text().strip().replace(",", ""),
    	}
    results.append(items)
    
# print(results)

#====csv 파일생성 utf처리======
with codecs.open("yaloja.csv", "wb", encoding="utf-8-sig") as f:
    header = ['title', 'price']
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    for item in results:
        w.writerow(item)




    
