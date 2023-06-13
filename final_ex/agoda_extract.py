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


#데이트 피커 많이 사용.
#모든 데이터는 엘리먼트가 있다 
#출발하는 날짜가 없다면 어떻게 할것인가 고민 
#화살표를 클릭했을 때 어떻게 나올 것인가? 
#셀레니움 응용 
#아이프레임으로 옮기는 것 
#레이징로딩 사이트(비어있는 엘리먼트가 있다)
#새탭으로 열렸음 






user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument('"detach", True')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
browser.maximize_window()

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



# pre_click=browser.find_element(By.CSS_SELECTOR, 'ul[role="listbox"]')
# pre_click.click()
# print("pre_click 클릭")

input=browser.find_element(By.CSS_SELECTOR,"#autocomplete-box input")
time.sleep(loading)
print("input 찾음")
input.click()

keyword="시드니"
pre_input.send_keys(keyword)
print("키워드 입력")


date_piker=browser.find_element(By.ID,"check-in-box").click()
print("date_piker 클릭")
time.sleep(loading)

in_day=browser.find_element(By.CSS_SELECTOR, 'span[data-selenium-date="2023-06-16"]')
print("date_piker 서치")
in_day.click()
print("in_day 클릭")

time.sleep(loading)
out_day=browser.find_element(By.CSS_SELECTOR, 'span[data-selenium-date="2023-07-02"]')
print("date_piker 서치")
out_day.click()
print("out_day 클릭")
time.sleep(loading)

search_btn=browser.find_element(By.CSS_SELECTOR, 'button[data-element-name="search-button"]')
search_btn.click()
time.sleep(loading)


#=====데이터 추출====== 

#그러면 나는 스크롤 다 내린 후에 마지막에 숩 열어 줄 필요가 있음
# 지금 나는 너무 혼재 되어있는 상태 위에서 스크롤 내리는거 세팅하고 숩으로 가져 오기 
last_page=2
page_num=1
while True:
    print("현재페이지", page_num)
    soup=BeautifulSoup(browser.page_source, "html.parser")
    # item_list=soup.select('ol.hotel-list-container')
    item_list=soup.select('a.PropertyCard__Link')
    element = browser.find_element(By.TAG_NAME,'body')
    time.sleep(loading)
    element.send_keys(Keys.PAGE_DOWN)
    option_list=[]
    for i in item_list:
        name=i.select_one('h3[data-selenium="hotel-name"]')
        if name:
            name=name.get_text().strip()
        else:
            name="이름없음"
        print("호텔명", name)
        
        element.send_keys(Keys.PAGE_DOWN)
        print("페이지다운")
        
        area= i.select_one('span.c-kEjbxe .sc-iqHYGH .bpoMrU .hGjjJo .sc-dQppl .cQZIoF')
        if area:
            area=area.get_text().strip()
        else:
            area="지역없음"
        print("지역", area)
        
        element.send_keys(Keys.PAGE_DOWN)
        print("페이지다운")
        
        price=i.select_one('span[data-selenium="display-price"]')
        if price:
            price=price.get_text().strip()
        else:
            price="가격없음"    
        print("가격", price,"\n")
          
        element.send_keys(Keys.PAGE_DOWN)
        print("페이지다운")
        
        #부모에서 gettext 해서 안에있는 모든 데이터 그냥 가지고 오기
        #굳이 리스트로 넣을 필요 없이 어차피 데이터 처리는 글자만 있으니면 되니까 
        options=i.select('div[data-selenium="pill-container"]')
        if options:
            for option in options:
                option_item=option.select_one('div[data-element-name="pill-each-item"]').get_text().strip()
                option_list.append(option_item)
        else:
            option="옵션없음"
        

    time.sleep(loading)
    element.send_keys(Keys.PAGE_DOWN)
    
        # for i in option_list:
        #     print(i)
    # page_num+=1
    # if page_num==last_page:
    #     break
    # try:
    #    next_page_ele=browser.find_element(By.ID, 'paginationNext')
    #    print(f"찾음 다음페이지 {page_num+1}")
    #    time.sleep(loading)
    #    next_page_ele.click()
    #    time.sleep(loading)
    #    print(f"클릭 다음페이지 {page_num+1}")
    #    #클릭 한후에는 와일문 처음으로 돌아 가고 위에 if 브레이크 만나기 전까지 계속 실행 
    # except:
    #     print(f"에러: 버튼 미추출 또는 미클릭 ******{page_num+1}")