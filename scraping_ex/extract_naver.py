#=====네이버블로그 검색+페이지네이션============#셀레니움 사용
# 1. 검색어(변화 無) 2. 기간(변화 無) 3. 페이지(변화 有)
# 쿼리를 건든다? 웹조작 페이지네이션에 대한 생각을 해보자
# 1~30p까지 가져온다면(1부터 끝까지가 아닌 30)
#메서드 사용시 라이브러리에서 요구사항을 그대로 따라줘야한다 
#내꺼보다 편하네 오호오호 왜 사람들이 안알려 줬을까? 너무 old 인가봐 

from selenium import webdriver
#크롬브라우저 접속 및 조작 
from selenium.webdriver.chrome.service import Service
#따로 받지 않아도 사용할 수 있데! 오 편한데~~ 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import  BeautifulSoup
import time

#======환경세팅================
#내 환경 알려주기(정상적인 접근이 아니라 똑같은 척 해야 함)
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
#셀레니움 옵션 객체 만들기 → 크롬한테 옵션 던지기 위한 옵션 세팅 
options=webdriver.ChromeOptions()
#헤드리스→ 조작 시 실제로 클릭하지 않아도 창 끄기(T)
options.add_argument('--headless=new')
#아규먼트 추가→  창 사이즈(≒모니터사이즈)
options.add_argument("window-size=1920x1080")
#아규먼트 추가→  유저에이전트 세팅 
options.add_argument(f"user-agent={user_agent}")   

#browser 변수명을 많이 사용 → 이제 자동화된 크롬브라우저
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
)
browser.maximize_window()           
# time.sleep(3000)            

#=====가져오는 것과 반복패턴 생각해 보기 =====
# 네이버블로그는 같이 카페는 혼자서 
#1 페이지의 1. area_list_search → find_all("div", class_="list_search_post") 추출 
#2 페이지로 이동 1-2는 반복 → for loop use(범위가 명확해서 사용)


#=====키워드 및 페이지세팅========
keyword="담꾹"
 #네이버의 패턴이 이렇게 생겨서 이렇게 쓰는것: 구글이라면 다르게 써야함
start_date="2022-01-01"        
end_date="2023-05-30"
# duration=1
#가져오는 페이지수 
# start_page=1
# end_date=3
pages=3

#====페이지 접근======
for page in range(pages):
    page_num=page+1     #페이지 넘버 세팅 첫번째는 1page가 될수 있게 +1부터 
    url=f"https://section.blog.naver.com/Search/Post.naver?pageNo={page_num}&rangeType=PERIOD&orderBy=sim&startDate={start_date}&endDate={end_date}&keyword={keyword}"
    browser.get(url) 
    time.sleep(3)  
    #====데이터추출하기======== 
    #브라우저 소스를 변화시켜서 가져 올 것이다. 
    soup= BeautifulSoup(browser.page_source, "html.parser")
    #부모 찾고 find_all 꼭 가지고 오기!! 잊어 버리지마 ㅠㅠㅠ 
    item_list=soup.find("div", attrs={"class":"area_list_search"}).find_all("div",class_="list_search_post")
    
    for i in item_list:
        title=i.find("span", class_="title").get_text().strip()
        print(title)
        





        
    time.sleep(5000)  


        

