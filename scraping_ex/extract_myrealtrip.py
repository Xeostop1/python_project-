from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv


#====마이리얼트립 iframe 사용하고 있음 
#효과적으로 다른 HTML 페이지를 현재 페이지에 포함시키는 중첩된 브라우저
# iframe 요소를 이용하면 해당 웹 페이지 안에 어떠한 제한 없이 다른 페이지를 불러와서 삽입 가능

# ====마이리얼트립 찾기 로직====
# 1. 검색어 구분이 되는 키워드로 공항코드 검색 
# 2. 검색어 구분이 되는 키워드로 공항코드 찾기
# 3. 로딩이 먼저 나타난다면 바로 보여줘(if)
# 4. iframe이라서 url+url→input찾고
# 5. 다시 돌아와서 검색값 찾기



user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--lang=ko-KR")
options.add_argument("lang=ko")
options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko_KR"})
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)

url="https://flights.myrealtrip.com/"
browser.get(url)
browser.maximize_window()
#iframe 때문에 사용함
f_page=browser.find_element(By.ID,"ifrSegSelect")
browser.switch_to.frame(f_page)
time.sleep(2)
#셀레니움 엘리먼트 찾아서 이동 여기서 input값 찾아야함
input=browser.find_element(By.ID,"depCtyCodeSearch")
input.click()
time.sleep(3)
#또 다른 프레임에 있어서 다시한번 브라우저 이동
browser.switch_to.default_content()

s_page=browser.find_element(By.ID,"_ifrm")
browser.switch_to.frame(s_page)

serch_input=browser.find_element(By.ID,"input_search")
keyword="SYD"
serch_input.click()
serch_input.send_keys(keyword)
time.sleep(3)
try:
    btn_serch=browser.find_element(By.ID, "btn_search")
    btn_serch.click()
    print("검색버튼 클릭")
    time.sleep(3)
except:
    print("검색버튼 찾지 못함")

    







