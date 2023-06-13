from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
#현재 날짜 가져오기 
from datetime import datetime
import time
import csv

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/89.0.4389.82 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent={}".format(user_agent))
browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
browser.maximize_window()


search_keyword = "노트북"
start_date = "2022.07.01"
end_date = "2022.07.14"
loading_duration = 1
pages = 3


#=======추가 부분=======csv추가 
#파이썬 현재날짜 추출하기 라이브러리로 검색해 보자! 
filename = f"네이버까페_{search_keyword}_검색결과_{datetime.today().strftime('%Y_%m_%d')}.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = "날짜,까페,제목,내용".split(",")
writer.writerow(title)

#2페이지 부터 시작하려면 1, 추가하면 시작점을 옮길 수 있음 
for page in range(pages):
    page_number = page + 1
    url = "https://cafe.naver.com/ca-fe/home/search/articles?q={}&p={}&pr=7&ps={}&pe={}".format(
        search_keyword,
        page_number,
        start_date,
        end_date,
    )

    browser.get(url)
    time.sleep(loading_duration)
    soup = BeautifulSoup(browser.page_source, "lxml")
    contents = soup.find_all("li", attrs={"class": "article_item"})

    for content in contents:
        date = content.find("span", attrs={"class": "write_date_time"}).get_text().strip()
        title = content.find("a", attrs={"class": "item_subject"}).get_text().strip()
        desc = content.find("p", attrs={"class": "item_content"}).get_text().strip()
        cafe = content.find("span", attrs={"class": "cafe_name"}).get_text().strip()
        data = [date, cafe, title, desc]
        print(data)
        writer.writerow(data)

#w,r 이라서 f 닫아보기  with까지 스면 굳이 닫지 않아도 된데 
f.close()
browser.quit()