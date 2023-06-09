from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import  BeautifulSoup
from selenium.webdriver.common.by import By
import time

#======환경세팅================
#내 환경 알려주기(정상적인 접근이 아니라 똑같은 척 해야 함)
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
options.add_argument('--headless')                              
options.add_argument("window-size=1920x1080")      
options.add_argument(f"user-agent={user_agent}")   

# #browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
)
browser.maximize_window()                        

#접속하는 함수 따로 만들기

# def extract_yalolja():
#     result=[]
#     items={}
#     #======셀레니움 세팅===============
#     user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
#     #셀레니움 옵션 객체 만들기 → 크롬한테 옵션 던지기 위한 옵션 세팅 
#     options=webdriver.ChromeOptions()
#     options.add_argument('--headless')  
#     options.add_argument("window-size=1920x1080")       
#     options.add_argument(f"user-agent={user_agent}")    

#     #browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
#     browser= webdriver.Chrome(
#         service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
#     )
#     browser.maximize_window()          
#     # time.sleep(3000)            
        
#     #=======bs4 파싱==============``
#     soup=BeautifulSoup(browser.page_source, "html.parser")
#     url="https://www.yanolja.com/leisure/list?mediumcat=10120006"
#     browser.get(url) 
#     time.sleep(5)  
#     #====데이터추출하기======== 
#     #브라우저 소스를 변화시켜서 가져 올 것이다. 
#     print("---------")
#     item_list=soup.select_one("div#__next")
    
#     # print(type(item_list))
#     print(item_list)
#     # for i in item_list:
#     #     print(i)
        
#     # pirce_list=soup.find_all("div", class_="LeisureListItem_body__1iNjJ")
#     # for i, j in zip(item_list, pirce_list):
#     #     items = {
#     #         "name": i.get_text().strip().replace(",", " "),
#     #         "price": j.get_text().strip().replace(",", " ")
#     #     }
#     #     result.append(items)
        
#     # return result

# extract_yalolja()

# 데이터 서칭까진 가능하고 스크롤만 해결 하면 끝

result=[]
items={}
#=======bs4 파싱==============
url="https://www.yanolja.com/leisure/list?mediumcat=10120006"
browser.get(url) 
time.sleep(3)  
#====데이터추출하기======== 
#브라우저 소스를 변화시켜서 가져 올 것이다. → 겟 하고와서 bs4로 추출 꼭 순서를 잊지 말자!→ 추출했엉 ㅠㅠㅠ 엉엉 얏호 얏호 
#===========스크롤 내리기=============== 브라우저get 가지고 와서 스크롤하고 bs4 하기 
prev_height = browser.execute_script("return document. body.scrollHeight")
#내꺼는 try문 에러 잡기 
while True:
	#첫번째로 스크롤 내리기
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	#시간대기
	time.sleep(2)
	#현재높이 저장
	current_height = browser.execute_script("return document. body.scrollHeight")
	#현재높이와 끝의 높이가 끝이면 탈출
	if current_height == prev_height:
		break
	#업데이트해줘서 끝낼 수 있도록 
	prev_height = current_height

soup=BeautifulSoup(browser.page_source, "html.parser")
#css 셀렉터 쓸 경우 꼭 다 붙여서 쓰자 
#두개를 쓰려면 더 큰 뎁스의 것을 가지고 오자! 이렇게 개별 단위로 가지고 오면 쓰기 어려움
item_list=soup.select("p.LeisureListItem_title__U-d8s")
pirce_list=soup.select("span.LeisurePriceDiscount_amount__19qBa")

# 그럼 두개다 넣으려면 크게 위에서 
# 어팬드 하는 방법 item_info.append([title,description,c_name,date])

for i in item_list:
    print(i.get_text().strip())
for i in pirce_list:
    print(i.get_text().strip())
    
