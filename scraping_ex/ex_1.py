from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user_agent={}".format(user_agent))
# options.add_argument(f"user-agent={user_agent}")



browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)
    )
browser.maximize_window()



# time.sleep(2000)

search_keyword = "눈영양제"
start_date = "2023-04-01"
end_date = "2023-05-30"
pages = 3


for page in range(pages):
    page_number = page + 1
    
    url = f"https://section.blog.naver.com/Search/Post.naver?pageNo={page_number}&rangeType=PERIOD&orderBy=sim&startDate={start_date}&endDate={end_date}&keyword={search_keyword}"
    
    browser.get(url)
    time.sleep(3)

    soup=BeautifulSoup(browser.page_source,"html.parser")
    divs=soup.find("div",attrs={"class":"area_list_search"}).find_all("div",attrs={"class":"list_search_post"})
    
    
    for div in divs:
        title=div.find("span",attrs={"class":"title"}).get_text().strip()
        print(title)