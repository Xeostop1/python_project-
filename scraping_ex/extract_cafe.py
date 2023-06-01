#타이틀, 설명
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

#deprecation: 이제 쓰지 않기 때문에 이 코드는 변경해 주세요→ 에러말고 경고정도 
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options=webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")   
browser= webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)  #생성자를 통해서 옵션전달하기 
)
browser.maximize_window()
#크게 열어놔야 우리가 시각적으로 본 것과 동일한 결과치가 나온다 



keyword="담꾹"
start_date="2022-01-01"
end_date="2023-05-30"
duration=1
pages=10
# start_page=3
# end_page=20
#range(star_page,end_page) 하면 페이지 부분 서칭이 가능(3~20)

#순서 까먹지 말기! 주소 → get → bs4파서 
item_info=[]

for page in range(pages):
    page_num=page+1
    url=f"https://section.cafe.naver.com/ca-fe/home/search/articles?q={keyword}&p={page_num}&pr=7&ps={start_date}&pe={end_date}"
    browser.get(url)
    time.sleep(3)
    soup= BeautifulSoup(browser.page_source, "html.parser")
    # item_list=soup.find("li", class_="article_item").find_all("div", class_="detail_area")
    item_list=soup.select("li.article_item")
    # item_list=soup.find_all("li", class_="article_item")
    
    count=0
    for i in item_list:
        count+=1
        title=i.find("a", class_="item_subject").get_text().strip()
        description=i.find("p", class_="item_content").get_text().strip()
        c_name=i.find("span", class_="cafe_name").get_text().strip()
        date=i.find("span", class_="write_date_time").get_text().strip()        
        # print(f"{count} 제목: {title} \n 설명: {description} \n {c_name} / {date}")
        item_info.append([title,description,c_name,date])

#===출력forloop=======
for i, item in  enumerate(item_info):
    print(f"{i+1} 제목: {item[0]}")
    print(f"내용: {item[1]}")
    print(f"카페: {item[2]}")
    print(f"날짜: {item[3]} \n")
    
#==========hrd-net========
# 셀렉터가 많은 mvc모델 웹페이지(일단 url이 엄청 길다)
#셀레니엄을 통해 키워드를 직접 넣고 하는 방법은 무엇인가?? → 사람이 실제로 하는것 처럼 검색어와 엔터를 치는 것(쿼리가 안먹어서)
#실행순서: 키워드검색→ 버튼실행 → 결과→ 페이지넘버 버튼실행→ 결과반복 
#쿼리가 안될때: 기본주소→ 검색창 클릭 → 검색어 입력(<input> > <textarea>) → 선택항목검색클릭 여기까지는 1번실행
#반복: 1. 1페이지에서 각 아이템 스크래핑 (for)
#     2. 페이지이동도 반복 (for) 그러나 똑같은 위치를 가질 수 없음(사람이 움직이면서 페이지버튼을 클릭 하기 때문에)


#=====다음영화 넷플릭스========
#상세주소페이지 저장 → 리스트에 저장 → 같은 패턴으로 클릭과 아이템 찾기 