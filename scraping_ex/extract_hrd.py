from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time



#==숙제: 바에 있는 엘리먼트 숫자를 넣고 취업률 없는 엘리먼트는 분기로 나누어서 취업률 없음 으로 변겅=====
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
# options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

url=f"https://www.hrd.go.kr/hrdp/ti/ptiao/PTIAO0300L.do?pageId=2&bgrlInstYn=undefined&kDgtlYn=undefined&_csrf=c59a9067-c598-4d31-bc31-fa1638d50d32"

browser.get(url)
#걸리는 시간이 있기 때문에 sleep 걸어줌
time.sleep(3)
#=====웹 조작====== 셀레니움 메서드 사용 /find_element(By.CSS_SELECTOR, "css selector") 이걸 많이 사용함(css식별자)[text="text"]
#셀레니엄야 엘리먼트 찾아줘 공공데이터를 상업적으로 사용 가능함 
element=browser.find_element(By.ID, "keyword")
keyword="sca"
element.send_keys(keyword)
#엔터처셔 검색하는 방식 keybord 누르기; 
# element.send_keys(Keys.ENTER)

time.sleep(3)
#**셀레니움은 예외처리 필요**
#엘리먼트를 찾기 못할 경우 오류 발생 근데 모두 셀레니움에 따라 다름!! try/carth 세팅 필요 셀레니움은 조작이라 다운이 되어버림 그래서 트라이캐치 꼭 필요!!
#=====셀레니움으로 버튼 클릭======
try:
    btn_elemnet=browser.find_element(By.CSS_SELECTOR, "button.loginBtn.btnType2")
    btn_elemnet.click()
except:
    #우회하는 코드를 적어도 다음 단계로 넘어 갈 수 있음 
    print("에러: 클릭 btn 엘레먼트 찾지 못함 ")

#=====bs4로 추출 ======= 와일로 추출 ㅠㅠ 으~ 싫어요 엉ㅇ어어어어엉
last_page=3
page_num=0
next_page=""

while True:
    page_num+=1
    print("현재페이지", page_num)
    soup=BeautifulSoup(browser.page_source, "html.parser")
    #부모 ul 접근
    info_list=soup.select(".detailList .content")
    
    #==타이틀 추출=====***에러 확인꼭 필요 왜 안되지???****
    for i, item in enumerate(info_list):
        #******이렇게는 안되고, .으로 안으로 들어가야돼 오류남 확인해 볼 것 *******
        title=item.select_one("p.tit").get_text().strip() 
        # title=item.p.a.get_text().strip()
        place_name=item.select_one("div.bar")["style"][6:-1]
        print(place_name)
        # print(place_name)
        # print(i+1,title)
    
    print(f"페이지 {page_num} 추출완료")
    #===다음페이지 세팅======위의 넥스트 페이지 보다 크다면 멈춰!
    # next_p_num=page_num+1
    # if next_p_num> last_page:
    
    #현재 페이지가 라시트 페이지랑 동일해도 → href /src 속성! 
    #css .# 빼고는 []으로 사용한다! 
    if page_num==last_page:
        break
    try:
       next_page_ele=browser.find_element(By.CSS_SELECTOR, f'a[href="?pageIndex={page_num+1}"]')
       print(f"찾음 다음페이지 {page_num+1}")
       next_page_ele.click()
       print(f"클릭 다음페이지 {page_num+1}")
       #클릭 한후에는 와일문 처음으로 돌아 가고 위에 if 브레이크 만나기 전까지 계속 실행 
    except:
        print(f"에러: 버튼 미추출 또는 미클릭 ******{page_num+1}")
    
    #LINK_TEXT :a안에 text 가져오기 
    
