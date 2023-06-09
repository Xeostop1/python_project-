from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

#====구분할 수 있게 코드 분리 작업 함수 작업 ====
#===셀레니움 파트==========
#구글 댓글 찾기 
#1.프리미엄 없애기(규칙찾기)
#2.스크롤 다운 
#3.댓글 버튼클릭() 엘레멘트 모두 가지고 와서 클릭 

# ====유튜브 찾기 로직====
# ------셀레니움------
# 1. 웹문서 접속
# 2. 스크롤 다운(1회성 작업 굳이 함수로 안만들어도 가능)
# 3. 답글 버튼 모두 찾기(if)
# 4. 답글 버튼 모두 *클릭
# 5. 서브코멘트 버튼 모두 찾기(if)
# 6. 서브코멘트 버튼 모두 *클릭 
# --------bs4---------
# 7. html 통채로 소스 가지고 오기
# 8. 페이지 분석 후 원하는 데이터만 추출
# 9. 엑셀파일 저장


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
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
        
        #새높
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
            #웹브라워저 웨이팅주는 코드 time.sleep랑 같음 
            commnet_block  = WebDriverWait(browser, 5).until(
                EC.presence_of_all_elements_located(
                    (
                        By.CSS_SELECTOR,
                        "div#contents > ytd-comment-thread-renderer > div#replies > ytd-comment-replies-renderer",
                    )
                )
            )
            print("댓글 더 보기 버튼 목록"+str(len(commnet_block))+"개 찾음")
            print("="*10)
            break
        except Exception as e:
            print(" 더 보기 버튼 못찾음 에러:",e)
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
        number_sub = 0
        while True:
            close_promotion()
            number_sub += 1
            is_more_sub_comment = ""

            try:
                is_more_sub_comment = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            "div#expander-contents > div#contents > ytd-continuation-item-renderer > div#button tp-yt-paper-button#button.style-scope.ytd-button-renderer[role='button']",
                        )
                    )
                )
                print(f"--{i + 1}번 댓글에는 서브 댓글이 존재합니다.")
            except:
                print(f"--{i + 1}번 댓글에는 서브 댓글이 존재하지 않습니다.")
                break

            try:
                is_more_sub_comment.click()
                print(f"--{i + 1}번 댓글의 서브 댓글 더 보기 {number_sub}번째 클릭 성공")
                time.sleep(loading + 4)
            except Exception as e:
                print(f"--{i + 1}번 댓글의 서브 댓글 더 보기 {number_sub}번째 클릭 실패")
                print(e)
                break

scroll_down()
click_more_commnets_btn(find_more_commnts_blocks())

#=====엑셀파일 생성(헤더추가)=======
file_name="youtube comment.csv"
f=open(file_name, "w", encoding="utf-8-sig", newline="")
w=csv.writer(f)
title="작성일,댓글 유형,좋아요 수, 댓글내용".split(".")
w.writerow(title)

#=====추출하기=======
#지금 나는 셀렉트가 모두 사용이 안돼ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ 왜 그럴까 확인해 보기 
soup=BeautifulSoup(browser.page_source,"html.parser")
comment_blocks=soup.find("ytd-comments", attrs={"id": "comments"}).find_all(
    "ytd-comment-thread-renderer",
    attrs={"class": "style-scope ytd-item-section-renderer"},
)
print(f"총{len(comment_blocks)}개 찾음")

#=====분류작업 일반댓글/서브댓글====for get_text()해야 에러가 나는것 없는것(None)은 에러가 나지 않음
#1. 부모중에 부모를 꺼냄 

for comment_block in comment_blocks:
    comment_boxes = comment_block.find_all(
        "ytd-comment-renderer",
        attrs={
            "class": [
                "style-scope ytd-comment-thread-renderer",
                "style-scope ytd-comment-replies-renderer",
            ]
        },
    )

    for comment_box in comment_boxes:
        comment_date = comment_box.find("div", attrs={"id": "header-author"}).find(
            "yt-formatted-string",
            attrs={"class": "published-time-text style-scope ytd-comment-renderer"},
        )

        if not comment_date:
            comment_date = "작성일 없음"
        else:
            comment_date = comment_date.get_text(strip=True)

        print("작성 시간 :", comment_date)

        try:  ## do not use this code
            comment_type = comment_box["id"]
        except:
            pass

        if comment_box.get("id") == "comment":
            comment_type = "일반 댓글"
        else:
            comment_type = "서브 댓글"

        print("댓글 유형 :", comment_type)







    
