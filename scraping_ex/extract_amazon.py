from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

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
extract_page=1

#=====페이지 접근======
for page in range(extract_page):
    page_num=page+1
    keyword="meal+kit"
    url=f"https://www.amazon.com/s?k={keyword}&page=3&crid=6IZDG33VVGY2&qid=1686288763&sprefix=%2Caps%2C867&ref=sr_pg_{page_num}"
    browser.get(url)
    time.sleep(3)
    soup=BeautifulSoup(browser.page_source, "html.parser")
    #--제일 큰 뎁스 찾기--
    item_list=soup.select("div.sg-col-inner")
    #---세부아이템 찾기----
    exchange=1292.79
    error_str="미 판매상품"
    for i,item in enumerate(item_list):
        #한개씩 찾아야 텍스트를 추출가능 까먹지 말기!! 
        whole_p=item.select_one("span.a-price-whole")
        if not whole_p:
            whole_p=error_str    
        else:
            whole_p=item.select_one("span.a-price-whole").get_text().strip()
        
        fraction_p=item.select_one("span.a-price-fraction")
        if not fraction_p:
            fraction_p=error_str    
        else:
            fraction_p=item.select_one("span.a-price-whole").get_text().strip()
        
        price=f"{whole_p}{fraction_p}"
        print(price)
        
        # k_price=float(price)*exchange
        # print(f"가격: {i+1}{price} /한국돈{k_price}")
        



