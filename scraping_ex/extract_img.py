from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

#====여러개의 웹문서 뎁스일 때 사용방법 a링크로 체이닝하기 ======
#숙제 → 구글 검색어 입력하고 광고빼고 타이틀, 날짜(none 이면 날짜 없음), 디스크립션까지 3페이지 추출 6/02 까지 

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options=webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")   
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)  
)
browser.maximize_window()
#까먹지 말아줘 ㅠㅠ 주소 → get → 추출

#클릭을 위해 상대주소 이용
url="https://movie.daum.net/premovie/netflix"
browser.get(url)
time.sleep(3)
soup=BeautifulSoup(browser.page_source,"html.parser")


#====다시!! 정리하기!!!========

m_url_list=[]
img_list=[]
origin_img_urls=[]

m_links=soup.select("a.thumb_item")



#=====1. 주소 가져오기 link =========
for i, itme in enumerate(m_links):
    num=i+1
    base_url="https://movie.daum.net"
    m_url=base_url+itme["href"]
    m_url_list.append(m_url)

#=====2. 이미지 주소 가져오기 ======
for i in m_url_list:
    #접속을 다시 함 → 겟을 했다?? 그러면 무조건 soup을 만들어서 실행해야 한다 → 그래야 파서가 된다!! 
    browser.get(i)
    time.sleep(0.5)
    soup=BeautifulSoup(browser.page_source,"html.parser")
    img_url=soup.select_one("div.info_poster").select("a.thumb_img")
    #오리지널로 가려고 이렇게 함 제일 큰 이미지로 바로 들어간 것 
    #Null 값이라면 if
    print(img_url["href"])
    # if img_url:
    #     origin_img_urls.append(i+img_url["href"])
    # else:
    #     continue
    #컨티뉴먼 다음 작업을 하고,  pass는 다음줄로 넘어감 

#=====3. 이미지 오리지널 가져오기========
for i, m_url in origin_img_urls:
    browser.get(m_url)
    time.sleep(0.5)
    soup=BeautifulSoup(browser.page_source,"html.parser")
    img_url=soup.select_one(".swiper-slide .swiper-slide-active").find("img", class_="img_thumb")
    
    if img_url:
        
    

    