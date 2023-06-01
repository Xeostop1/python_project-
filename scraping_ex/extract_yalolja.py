from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import  BeautifulSoup
from selenium.webdriver.common.by import By
import time

#======환경세팅================
#내 환경 알려주기(정상적인 접근이 아니라 똑같은 척 해야 함)
# user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

# options=webdriver.ChromeOptions()
# options.add_argument('--headless')                               #헤드리스→ 조작 시 실제로 클릭하지 않아도 창 끄기(T)
# options.add_argument("window-size=1920x1080")       #아규먼트 추가→  창 사이즈(≒모니터사이즈)
# options.add_argument(f"user-agent={user_agent}")    #아규먼트 추가→  유저에이전트 세팅

# #browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
# browser= webdriver.Chrome(
#     service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
# )
# browser.maximize_window()           
# time.sleep(3000)                   

#===========스크롤 내리기===============
# prev_height = browser.execute_script("return document. body.scrollHeight")
# while True:
# 	#첫번째로 스크롤 내리기
# 	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 	#시간대기
# 	time.sleep(2)
# 	#현재높이 저장
# 	current_height = browser.execute_script("return document. body.scrollHeight")
# 	#현재높이와 끝의 높이가 끝이면 탈출
# 	if current_height == prev_height:
# 		break
# 	#업데이트해줘서 끝낼 수 있도록
# 	prev_height = current_height


def extract_yalolja():
    result=[]
    items={}
    #======셀레니움 세팅===============
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    #셀레니움 옵션 객체 만들기 → 크롬한테 옵션 던지기 위한 옵션 세팅 
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')  
    options.add_argument("window-size=1920x1080")       
    options.add_argument(f"user-agent={user_agent}")    

    #browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
    browser= webdriver.Chrome(
        service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
    )
    browser.maximize_window()          
    # time.sleep(3000)            
        
    #=======bs4 파싱==============``
    soup=BeautifulSoup(browser.page_source, "html.parser")
    url="https://www.yanolja.com/leisure/list?mediumcat=10120006"
    browser.get(url) 
    time.sleep(5)  
    #====데이터추출하기======== 
    #브라우저 소스를 변화시켜서 가져 올 것이다. 
    # item_list=soup.find("section", attrs={"class":"LeisureMediumCategories_container__3CIkg"})
    item_list=soup.select("div .LeisureMediumCategories_wrap__34oLX")
    print(type(item_list))
    print(len(item_list))
    # for i in item_list:
    #     print(i)
        
    pirce_list=soup.find_all("div", class_="LeisureListItem_body__1iNjJ")
    # for i, j in zip(item_list, pirce_list):
    #     items = {
    #         "name": i.get_text().strip().replace(",", " "),
    #         "price": j.get_text().strip().replace(",", " ")
    #     }
    #     result.append(items)
        
    # return result

extract_yalolja()


