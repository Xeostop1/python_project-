from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

#====구분할 수 있게 코드 분리 작업 함수 작업 ====
#===셀레니움 파트==========
#구글 댓글 찾기 
#1.프리미엄 없애기(규칙찾기)
#2.스크롤 다운 
#3.댓글 버튼클릭() 엘레멘트 모두 가지고 와서 클릭 


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--lang=ko-KR")
options.add_argument("lang=ko")
options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko_KR"})
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()

url="https://www.youtube.com/watch?v=UROWQ1VwVYQ"
loading=2
max_height=5000
browser.get(url)

#===프로모션팝업창 닫기=======
def close_promotion():
    try:
        browser.find_element(By.CSS_SELECTOR, "yt-button-renderer#dismiss-buttion").click()
        print("팝업닫기")
    except:
        pass

#===스크롤 다운=======
def scroll_down():
    #바로 들어와서 바로 보이는 첫번째 높이 가져오기 
    old_h=browser.execute_script("return document.documentElement.scrollHeight")
    num=0
    
    while True:
        num+=1
        print("이전 웹 문서 높이", old_h)
        print(f"스크롤 아래로 {num}회차 ")
        #문서높이 만큼 
        cur_h="document.documentElement.scrollHeight"
        
        browser.execute_script(f"window.scrollTo(0,{cur_h})")
        print("최하단")
        time.sleep(loading) 
        #툴팁((좋아요 손모양))때문에 이벤트 때문에 깨긋한 화면으로 만든 상태(오류없이 살짝 올려준 상태)
        loading_h=600   
        browser.execute_script(f"window.scrollTo(0,{loading_h})")
        print("상단에서 +600")
        time.sleep(loading)
        new_h=browser.execute_script(f"return {cur_h}")
        
        #새높이
        if new_h==old_h or new_h>=max_height:
            print("=====스크롤 작업완료======")
            break 
        old_h=new_h
        #다시 떳으면 프로모션 닫기 
        close_promotion()
    
#===블럭 찾기=====
def find_more_commnts_blocks():
    while True:
        close_promotion()
        try:
            commnet_block=WebDriverWait(browser,5).until(EC.presence_of_all_elements_located(By.CSS_SELECTOR,  
                                                                                             "div#contents > ytd-comment-thread-renderer > div#replies > ytd-comment-replies-renderer"
            ))
            print("댓글 더 보기 버튼 목록"+str(len(commnet_block))+"개 찾음")
            print("="*10)
            break
        except Exception as e:
            print("못찾음 에러:",e)
            print("*"*10)
    return commnet_block


#====블럭내 버튼 찾기=====
def click_more_commnets_btn(commnet_block):
    close_promotion()
    for i, commnet_block in enumerate(commnet_block):
        try:
            more_click_btn=commnet_block.find_element(By.CSS_SELECTOR, "div#expander ytd-button-renderer#more-replies")
            print(f"대댓글btn{i+1}번 찾기성공")
            #js에서 바로 클릭하는 메서드(click())
            browser.execute_script("arguments[0].click()",more_click_btn)
            print(f"대댓글btn{i+1}번 클릭성공")
            time.sleep(loading+2)
        except Exception as e:
            print(f"클릭 또는 찾기 에러 {i+1}번")
            print("에러: ",e)
            try:
                browser.execute_script("window.scrollTo(0,700)")
                print("에러로 다시 살짝 스크롤 업 다시 시작")
                click_more_commnets_btn(find_more_commnts_blocks())
                break
            except Exception as e:
                print("다시찾기 과정중 에러:", e)