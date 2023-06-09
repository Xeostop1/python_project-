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





#====웹조작=======
url=f"https://www.amazon.com/ref=nav_logo"
keyword="meal kit"



def control_amazon(url,keyword):
    browser.get(url)    
    time.sleep(3)
    input=browser.find_element(By.ID,"twotabsearchtextbox")
    input.send_keys(keyword)
    time.sleep(3)
    try:
        btn_search=browser.find_element(By.ID,"nav-search-submit-button")
        btn_search.click()
        time.sleep(2)
    except Exception as e:
        print("검색클릭 오류:", e)



control_amazon(url,keyword)


#===아이템 저장====
results=[]
items={}

#===페이지 세팅===
last_page=7
page_num=0
next_page=""


def find_item(items):
    exchange=1292.79
    error_str="미 판매상품"
    price=0
    k_price=1
    
    for i,item in enumerate(items):
        #한개씩 찾아야 텍스트를 추출가능 까먹지 말기!! 
        whole_p=item.select_one("span.a-price-whole")
        fraction_p=item.select_one("span.a-price-fraction")
        star=item.select_one("span.a-icon-alt")
    #====추출======
    while True:
        page_num+=1
        print("현재페이지", page_num)
        soup=BeautifulSoup(browser.page_source, "html.parser")
        #=====페이지 접근======
        #--제일 큰 뎁스 찾기--
        item_list=soup.select("div.a-section.a-spacing-base")
        for i,item in enumerate(item_list):
            #한개씩 찾아야 텍스트를 추출가능 까먹지 말기!! 
            whole_p=item.select_one("span.a-price-whole")
            fraction_p=item.select_one("span.a-price-fraction")
            star=item.select_one("span.a-icon-alt")
            #---가격---
            if not whole_p:
                whole_p=error_str    
                fraction_p=error_str
            else:
                whole_p=item.select_one("span.a-price-whole").get_text().strip()
                fraction_p=item.select_one("span.a-price-fraction").get_text().strip()
                price=f"{whole_p}{fraction_p}"
                k_price=exchange*float(price)
                items={
                    "product":item.select_one("span.a-size-base-plus.a-color-base.a-text-normal").get_text().strip(),
                    "price":float(price),
                    "k_price":round(k_price,1)
                }
            #--별점---
            if not star:
                star=error_str
            else:
                items["star"]=star=item.select_one("span.a-icon-alt").get_text()[0:4].strip()
                results.append(items)
                
                
last_page = 7

def page_move(last_page):
    page_num = 0
    next_page = ""
    while page_num < last_page:  # page_num이 last_page보다 작을 때까지 반복
        try:
            next_page = browser.find_element(By.CLASS_NAME, ".s-pagination-item.s-pagination-button")
            print(f"다음 페이지 찾음: {page_num + 1}")
            next_page.click()
            print(f"다음 페이지로 이동: {page_num + 1}")
        except Exception as e:
            print(f"오류 발생: 버튼 추출 또는 클릭 실패 ******{page_num + 1}")
        page_num += 1  # 반복문 내에서 page_num을 증가시킴





    



print(tuple(results))
#====csv 파일생성 utf처리======
with codecs.open("amazon_product_list.csv", "wb", encoding="utf-8-sig") as f:
    header = ["product", "price","k_price","star"]
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    for item in results:
        w.writerow(item)



