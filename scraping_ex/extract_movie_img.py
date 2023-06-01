from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent={}".format(user_agent))


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = "https://movie.daum.net/premovie/netflix?flag=C"
browser.get(url)
time.sleep(3)

soup=BeautifulSoup(browser.page_source, "html.parser")
moive_links=soup.select("a.thumb_item")

movie_list=[]
m_img_list=[]
origin_img_list=[]

#======무비링크 추출=======
for i, m_link in enumerate(moive_links):
    num=i+1
    m_url="https://movie.daum.net" + m_link['href']    
    movie_list.append(m_url)


#====무비포스터 섬네일 접근======= movie_urls 다시 숩객체 생성
for i in movie_list:
    browser.get(i)
    time.sleep(0.5)
    soup=BeautifulSoup(browser.page_source, "html.parser")
    #진짜 이미지 추출되는 곳
    img_url=soup.find("div", attrs={"class": "info_poster"}).find("a", attrs={"class": "thumb_img"})
    if img_url:
        m_img_list.append(i+img_url["href"])
    else:
        print("error")
        continue

for i, m_img_url in enumerate(m_img_list):
    browser.get(m_img_url)
    time.sleep(0.5)
    soup=BeautifulSoup(browser.page_source,"html.parser")
    origin_img_url=soup.select_one(".swiper-slide.swiper-slide-active").find("img", attrs={"class": "img_thumb"})["src"]
    origin_img_list.append(m_img_url)
    


for i in origin_img_list:
    print(i,"\n")