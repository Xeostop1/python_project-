from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random



#==숙제: 바에 있는 엘리먼트 숫자를 넣고 취업률 없는 엘리먼트는 분기로 나누어서 취업률 없음 으로 변겅=====
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

loading = random.randint(5, 12)

# ====아고다======
#결과물이 새창이 뜨는 형태 탭이동(JS나 쿼리로 이동해야 되나? 그건 하지 않는데~)
#스크롤을 한번 내려야 아이템이 뜨는 경우가 있기 때문에 스크롤 작업 한번 해주기 (검색결과 없으면 처리필요) 

#div→ 클릭

url="https://www.agoda.com/ko-kr/"

browser.get(url)
time.sleep(loading)
pre_input=browser.find_element(By.ID, "autocomplete-box")
print("pre_input 찾기")
pre_input.click()
print("pre_input 클릭")
time.sleep(loading)
input=browser.find_element(By.ID,"textInput")
print("input 찾기")
input.click()
print("input 클릭")
