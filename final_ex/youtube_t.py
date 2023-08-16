# 유튜브 코멘트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument(f"user-agent={user_agent}")
# options.add_argument("--headless")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
browser.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """
    },
)
browser.maximize_window()

url = "https://www.youtube.com/watch?v=mVdyQ60DVPU"
browser.get(url)

loading_duration = 2
max_height = 3000


# 프로모션 팝업창 닫기 함수
def close_promotion():
    try:
        browser.find_element(By.CSS_SELECTOR, "yt-button-renderer#dismiss-button").click()
        print("############## 프리미엄 팝업창을 닫았습니다. ##############")
    except:
        pass


# 스크롤 다운 함수
def scroll_down():
    old_height = browser.execute_script("return document.documentElement.scrollHeight")
    number = 0

    while True:
        number += 1
        print("이전 웹문서 높이(px)", old_height)
        print(f"스크롤 아래로 내리기 {number}회차 접어듭니다.")

        browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        print("스크롤을 최하단까지 내렸습니다.")
        time.sleep(loading_duration)

        browser.execute_script("window.scrollTo(0, 600)")
        print("스크롤을 상단에서 600px 높이까지 올렸습니다.")
        time.sleep(loading_duration)

        new_height = browser.execute_script("return document.documentElement.scrollHeight")

        if new_height == old_height or new_height >= max_height:
            print("############## 스크롤 작업이 완료되었습니다. ##############")
            break

        old_height = new_height

        close_promotion()


def find_more_comments_blocks():
    while True:
        close_promotion()

        try:
            more_comment_blocks = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#contents > ytd-comment-thread-renderer > div#replies > ytd-comment-replies-renderer")))
            
            print("댓글 더 보기 버튼 목록" + str(len(more_comment_blocks)) + "개 찾았음")
            print("-" * 100)
            break
        except:
            print("댓글 더 보기 버튼 목록 못 찾았음")
            print("-" * 100)

    return more_comment_blocks


def click_more_comments_button(more_comment_blocks):
    close_promotion()
    
    for i, more_comment_block in enumerate(more_comment_blocks):
        try:
            more_click_button = more_comment_block.find_element(By.CSS_SELECTOR, "div#expander ytd-button-renderer#more-replies")
            print(f"댓글 더 보기 {i + 1}번 찾기 성공")
#             more_click_button.click()
            browser.execute_script("arguments[0].click();", more_click_button)
            print(f"댓글 더 보기 {i + 1}번 클릭 성공")
            time.sleep(loading_duration + 2)
            #add: 버튼의 위치를 js높이를 찾음
            browser.execute_script("window.scrollTo(0,arguments[0])",int(more_comment_block.location["y"]))
            time.sleep(loading_duration + 2)
            #add: 300을 추가한 이유는 살짝 움직여서 버튼을 로딩되게 만듬
            browser.execute_script("window.scrollTo(0,arguments[0])+300",int(more_comment_block.location["y"]))
        except Exception as e:
            print(f"댓글 더 보기 {i + 1}번 찾기 또는 클릭 실패")
            print("에러 메세지 :", e)

            try:
                browser.execute_script("window.scrollTo(0, 700)")
                print("댓글 더 보기 찾기 또는 클릭 에러가 발생하여 스크롤을 살짝 위로 올린 후 다시 시도합니다.")
                click_more_comments_button(find_more_comments_blocks())
                break
            except Exception as ex:
                print("에러 메세지 :", ex)

        number_sub = 0
        while True:
            close_promotion()

            number_sub += 1
            is_more_sub_comment = ""

            try:
                is_more_sub_comment = more_comment_block.find_element(By.CSS_SELECTOR, "ytd-continuation-item-renderer div#button > ytd-button-renderer yt-button-shape > button")
                print(f"--{i + 1}번 댓글에는 서브 댓글이 존재합니다.")
            except:
                print(f"--{i + 1}번 댓글에는 서브 댓글이 존재하지 않습니다.")
                break

            try:
                browser.execute_script("arguments[0].click();", is_more_sub_comment)
                print(f"--{i + 1}번 댓글의 서브 댓글 더 보기 {number_sub}번째 클릭 성공")
                browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight - 300)")
                time.sleep(loading_duration + 4)
            except Exception as e:
                print(f"--{i + 1}번 댓글의 서브 댓글 더 보기 {number_sub}번째 클릭 실패")
                print(e)
                break


scroll_down()
click_more_comments_button(find_more_comments_blocks())


# 1. 웹문서 접속
# 2. 스크롤 다운
# 3. comment 버튼 모두 찾기
# 4. comment 버튼 모두 클릭 / sub_comment 버튼 모두 찾기 / sub_comment 버튼 모두 클릭
# 7. 페이지 소스 가지고 오기
# 8. 페이지 소스 분석해서 원하는 데이터만 추출하기
# 9. 엑셀 파일로 저장


filename = "유튜브 코멘트.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = "작성일,댓글 유형,좋아요 수,댓글 내용".split(",")
title = ["작성일", "댓글 유형", "좋아요 수", "댓글 내용"]
writer.writerow(title)

soup = BeautifulSoup(browser.page_source, "lxml")
comment_blocks = soup.find("ytd-comments", attrs={"id": "comments"}).find_all("ytd-comment-thread-renderer", attrs={"class": "style-scope ytd-item-section-renderer"})

print(f"총 {len(comment_blocks)}의 댓글 블록을 가져왔습니다.")

for comment_block in comment_blocks:
#     comment_boxes = comment_block.find_all("ytd-comment-renderer", attrs={"class": ["style-scope ytd-comment-thread-renderer", "style-scope ytd-comment-replies-renderer"]})
    comment_boxes = comment_block.find_all("ytd-comment-renderer")

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

        if comment_box.get("id") == "comment":
            comment_type = "일반 댓글"
        else:
            comment_type = "서브 댓글"

        print("댓글 유형 :", comment_type)

        comment_like = comment_box.find("span", attrs={"id": "vote-count-middle"})

        if not comment_like:
            comment_like = "0"
        else:
            comment_like = comment_like.get_text(strip=True)

        print("좋아요 수 :", comment_like)

        comment_content = comment_box.find("yt-formatted-string", attrs={"id": "content-text"})

        if not comment_content:
            comment_content = "댓글 내용 없음"
        else:
            comment_content = comment_content.get_text(strip=True)

        print("댓글 내용 :", comment_content)
        print("-" * 80)

        data = [comment_date, comment_type, comment_like, comment_content]
        writer.writerow(data)


time.sleep(loading_duration)

f.close()
browser.quit()