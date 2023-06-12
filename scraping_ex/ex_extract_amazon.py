from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv
import codecs
import random 

rand_value = random.randint(1, 8)
time.sleep(rand_value)


#====웹컨트롤======
def control_amazon(url, keyword):
    browser.get(url)
    time.sleep(rand_value)
    input_element = browser.find_element(By.ID, "twotabsearchtextbox")
    input_element.send_keys(keyword)
    time.sleep(rand_value)
    try:
        btn_search = browser.find_element(By.ID, "nav-search-submit-button")
        btn_search.click()
        time.sleep(rand_value)
    except Exception as e:
        print("검색클릭 오류:", e)



# ====데이터추출=====
def find_item(results):
    exchange = 1292.79
    error_str = "미 판매상품"
    
    next_page = browser.find_element(By.CSS_SELECTOR, ".s-pagination-item.s-pagination-button")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    item_list = soup.select("div.a-section.a-spacing-base")

    for item in item_list:
        whole_p = item.select_one("span.a-price-whole")
        fraction_p = item.select_one("span.a-price-fraction")
        star = item.select_one("span.a-icon-alt")

        if not whole_p:
            whole_p = error_str
            fraction_p = error_str
        else:
            whole_p = item.select_one("span.a-price-whole").get_text().strip()
            fraction_p = item.select_one("span.a-price-fraction").get_text().strip()
            price = f"{whole_p}{fraction_p}"
            k_price = exchange * float(price)
            items = {
                "product": item.select_one("span.a-size-base-plus.a-color-base.a-text-normal").get_text().strip(),
                "price": float(price),
                "k_price": round(k_price, 1)
            }
            if not star:
                star = error_str
            else:
                items["star"] = star = item.select_one("span.a-icon-alt").get_text()[0:4].strip()
            results.append(items)



# ====CSV로 저장하기 위한 함수====
def save_to_csv(results):
    with codecs.open("amazon_product_list.csv", "w", encoding="utf-8-sig") as f:
        header = ["product", "price", "k_price", "star"]
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(results)


# =====주실행부======
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--lang=ko-KR")
options.add_argument("lang=ko")
options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko_KR"})
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()

url = "https://www.amazon.com/ref=nav_logo"
keyword = "meal kit"

control_amazon(url, keyword)
results = []
find_item(results,last_page=10)
save_to_csv(results)
browser.quit()
