#타이틀, 설명
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options=webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")   
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
)
browser.maximize_window() 

keyword="담꾹"
start_date="2022-01-01"
end_date="2023-05-30"
pages=3

for page in range(pages):
    page_num=page+1
    url=f"https://section.cafe.naver.com/ca-fe/home/search/articles?q={keyword}&pr=7&ps={start_date}&pe={end_date}"
    browser.get(url)
    time.sleep(3)
    soup= BeautifulSoup(browser.page_source, "html.parser")
    item_list=soup.find("ul", class_="ArticleList").find_all("div", class_="detail_area")
    
    count=0
    for i in item_list:
        count+=1
        title=i.find("a", class_="item_subject").get_text().strip()
        description=i.find("p",class_="item_content").get_text().strip()
        print(f"{count} 제목: {title} / 설명: {description}")
    