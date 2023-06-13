from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
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
start_date = "2023-04-01"
end_date = "2023-05-14"
duration = 1
pages = 3


#=======추가 부분=======csv추가 
filename = f"네이버블로그_{search_keyword}_검색결과_{datetime.today().strftime('%Y_%m_%d')}.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = "날짜,제목,내용".split(",")
writer.writerow(title)


for page in range(pages):
    page_number = page + 1
    url = "http://section.blog.naver.com/Search/Post.nhn?pageNo={}&rangeType=ALL&startDate={}&endDate={}&orderBy=sim&keyword={}".format(
        page_number, start_date, end_date, search_keyword
    )
    browser.get(url)
    time.sleep(duration)
    soup = BeautifulSoup(browser.page_source, "lxml")
    contents = soup.find_all("div", attrs={"class": "list_search_post"})

    for content in contents:
        date = content.find("span", attrs={"class": "date"}).get_text().strip()
        title = content.find("strong", attrs={"class": "title_post"}).get_text().strip()
        desc = content.find("a", attrs={"class": "text"}).get_text().strip()
        data = [date, title, desc]
        print(data)
        writer.writerow(data)

f.close()
browser.quit()