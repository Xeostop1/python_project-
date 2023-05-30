from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import  BeautifulSoup
import time

#======환경세팅================
#내 환경 알려주기(정상적인 접근이 아니라 똑같은 척 해야 함)
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
#셀레니움 옵션 객체 만들기 → 크롬한테 옵션 던지기 위한 옵션 세팅 
options=webdriver.ChromeOptions()
options.headless=True                               #헤드리스→ 조작 시 실제로 클릭하지 않아도 창 끄기(T)
options.add_argument("window-size=1920x1080")       #아규먼트 추가→  창 사이즈(≒모니터사이즈)
options.add_argument(f"user-agent={user_agent}")    #아규먼트 추가→  유저에이전트 세팅

#browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
)
browser.maximize_window()           #
time.sleep(3000)                    #

#===========스크롤 내리기===============
prev_height = browser.excute_script("return document. body.scrollHeight")
import time
while True:
	#첫번째로 스크롤 내리기
	browser.excute_script("window.scrollTo(0,document.body.scrollHeight)")
	#시간대기
	time.sleep(2)
	#현재높이 저장
	current_height = browser.excute_script("return document. body.scrollHeight")
	#현재높이와 끝의 높이가 끝이면 탈출
	if current_height == prev_height:
		break
	#업데이트해줘서 끝낼 수 있도록
	prev_height == current_height



def extract_yalolja():
    result=[]
    items={}
    #======셀레니움 세팅===============
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    #셀레니움 옵션 객체 만들기 → 크롬한테 옵션 던지기 위한 옵션 세팅 
    options=webdriver.ChromeOptions()
    options.headless=True                               #헤드리스→ 조작 시 실제로 클릭하지 않아도 창 끄기(T)
    options.add_argument("window-size=1920x1080")       #아규먼트 추가→  창 사이즈(≒모니터사이즈)
    options.add_argument(f"user-agent={user_agent}")    #아규먼트 추가→  유저에이전트 세팅

    #browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
    browser= webdriver.Chrome(
        service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
    )
    browser.maximize_window()           #
    time.sleep(3000)                    #
        
    #=======bs4 파싱==============
    soup=BeautifulSoup(browser.page_source, "html.parser")
    item_list=soup.find_all("p", class_="LeisureListItem_title__U-d8s")
    pirce_list=soup.find_all("span", class_="LeisurePriceDiscount_amount__19qBa")
    for i in item_list:
        for j in pirce_list:

            items={
                #soup 객체라서 메서드 사용가능 
                "name":i.get_text().strip().replace(",", " "),
                "pirce":j.get_text().strip().replace(",", " ")
            }
        result.append(items)
        
    return result

res=extract_yalolja()
print(res)