from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--lang=ko-KR")
# options.add_argument("lang=ko")
# options.add_experimental_option("prefs", {"intl.accept_languages": "ko,ko_KR"})
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
browser.maximize_window()

url = "https://play.google.com/store/apps/details?id=com.kakao.talk"
browser.get(url)
max_height = 5000



#========스크롤다운==========execute_script:직접 자바스크립트 코드를 조작 
def scroll_down(modal):
    
    try:
        print(f"{num}회차 진행")
        #현재 높이(바로 보이는 높이=기존높이)
        old_height = browser.execute_script("return arguments[0].scrollHeight", modal)
        new_height=0
        num=0
        while True:
            num+=1
            #처음 사이즈와같은지 확인 
            if new_height == old_height or new_height >= max_height:
                print("스크롤 완료")
                break
            #scrollTo움직여라 아규먼트0부터 높이까지(파라미터:모달)
            browser.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight);", modal
            )
            time.sleep(1)
            browser.execute_script(
                #자동으로 하는 것이라서 -100만큼 위로 살짝올려줌 
                "arguments[0].scrollTo(0, arguments[0].scrollHeight-100);", modal
            )
            time.sleep(1)
            #달라진것을 찾기 위해 new찾기 
            new_height = browser.execute_script("return arguments[0].scrollHeight", modal)
            try:
                all_review_button = browser.find_element(
                    By.CSS_SELECTOR,
                    "#ow94 button.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.QDwDD.mN1ivc.VxpoF",
                ).click()
                
                print("old", old_height)
                print("new", new_height)
            except:
                if new_height == old_height or new_height >= max_height:
                    print("스크롤 완료")
                    break
                old_height = new_height
        print(new_height)

    except Exception as e:
        print("스크롤링 도중 에러 발생: ", e)
all_review_button_xpath = '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/c-wiz[4]/section/header/div/div[2]/button'



while True:
    try:
        modal=WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, all_review_button_xpath)))
        print("리뷰 모두 보기 버튼 발견")
        browser.find_element(By.XPATH, all_review_button_xpath).click()
        print("리뷰 모두 보기 버튼 클릭")
        break
    except Exception as e:
        print("리뷰 모두 보기 버튼 탐색 또는 클릭 도중 에러 발생")
        print(e)


scroll_down(modal)

soup=BeautifulSoup(browser.page_source,"html.parser")
browser.quit()


#======추출=========
review_list=soup.select("div.RHo1pe")
num=0
for i in review_list:
    num+=1
    #====데이터=====
    date=i.select_one("span.bp9Aid").get_text().strip()
    user_name=i.select_one("div.X5PpBb").get_text().strip()
    # star=i.select("div.iXRFPc")["aria-label"][10]
    content=i.select_one("div.h3YV2d").get_text().strip()
    print("날짜: ",date)
    print("이름: ",user_name)
    # print("별점: ",star)
    print("컨텐트: ",content)
    


#구글 특이한 부분찾기 이상오류 찾아오기 