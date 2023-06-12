from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random



#==숙제: 바에 있는 엘리먼트 숫자를 넣고 취업률 없는 엘리먼트는 분기로 나누어서 취업률 없음 으로 변겅=====
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument('"detach", True')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

loading = random.randint(5, 12)
wait = WebDriverWait(browser, 10)

# ====아고다======
#결과물이 새창이 뜨는 형태 탭이동(JS나 쿼리로 이동해야 되나? 그건 하지 않는데~)
#스크롤을 한번 내려야 아이템이 뜨는 경우가 있기 때문에 스크롤 작업 한번 해주기 (검색결과 없으면 처리필요) 

#div→ 클릭

url="https://www.agoda.com/ko-kr/search?city=3435&checkIn=2023-06-21&los=28&rooms=1&adults=2&children=0&cid=1908612&locale=ko-kr&ckuid=a2cbcb12-1461-4bd1-a206-f014cd919d35&prid=0&currency=KRW&correlationId=e0428ddf-5da7-415e-a7e8-533c13940c49&analyticsSessionId=5422511383678882083&pageTypeId=1&realLanguageId=9&languageId=9&origin=KR&userId=a2cbcb12-1461-4bd1-a206-f014cd919d35&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=26&currencyCode=KRW&htmlLanguage=ko-kr&cultureInfoName=ko-kr&machineName=hk-pc-2f-acm-web-user-66b6887b57-9vr9z&trafficGroupId=4&sessionId=i0zlfmp05qfq2wlqogryxjqr&trafficSubGroupId=849&aid=296180&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-07-19&priceCur=KRW&textToSearch=%EC%82%BF%ED%8F%AC%EB%A1%9C&travellerType=1&familyMode=off&productType=-1"

browser.get(url)
time.sleep(loading)

pre_input=browser.find_element(By.ID,"autocomplete-box")
print("pre_input 찾음")
pre_input.click()
print("pre_input 클릭")
time.sleep(loading)

keyword="시드니"
pre_input.send_keys(keyword)
print("키워드 입력")

# pre_click=browser.find_element(By.CSS_SELECTOR, 'ul[role="listbox"]')
# pre_click.click()
# print("pre_click 클릭")

input=browser.find_element(By.CSS_SELECTOR,"#autocomplete-box input")
time.sleep(loading)
print("input 찾음")
input.click()

date_piker=browser.find_element(By.ID,"check-in-box").click()
print("date_piker 클릭")
time.sleep(loading)

in_day=browser.find_element(By.CSS_SELECTOR, 'span[data-selenium-date="2023-06-12"]')
print("date_piker 서치")
in_day.click()
print("in_day 클릭")

time.sleep(loading)
out_day=browser.find_element(By.CSS_SELECTOR, 'span[data-selenium-date="2023-07-19"]')
print("date_piker 서치")
out_day.click()
print("out_day 클릭")
time.sleep(loading)

search_btn=browser.find_element(By.CLASS_NAME, "Searchbox__searchButton__text")
search_btn.click()



#=====데이터 추출====== 

while True:
    page_num=1
    print("현재페이지", page_num)
    soup=BeautifulSoup(browser.page_source, "html.parser")
    item_list=soup.select('ol.hotel-list-container')
    for i in item_list:
        print(i)