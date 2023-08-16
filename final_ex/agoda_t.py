from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random
#===선생님은 아고다에서 바로 했음=====

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent={}".format(user_agent))
browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

url = "https://www.agoda.com/ko-kr/"
browser.get(url)
browser.maximize_window()

destination = "시드니"
departure_date = "2023-06-24"
return_date = "2023-07-24"
#====랜덤으로 변경=========
loading_duration = random.randint(5,25)
pages = 14


#=======광고팝업 삭제======
def close_ad():
    try:
        browser.find_element(By.CSS_SELECTOR, "button.ab-close-button").click()
    except Exception as e:
        # 에러때문에 pass 사용 
        pass


result_container = []

#서브 키워드를 나눠서 메인키워드는 무조건 검색하고 if로 서브키워드가 있다면 
#그 엘리먼트를 선택해라
try:
    #====선생님은 계속 덮어쓰는 것으로 선택함=====
    #===가끔 #가 여러개 인것도 있데 ======
    element = browser.find_element(By.CSS_SELECTOR, "input#textInput")
    print("input 엘리먼트 찾음")
    element.send_keys(destination)
    print(f'input 엘리먼트에 "{destination}" 입력')

    #=====이거말고 드라이버웨잇 언틸사용=====
    time.sleep(loading_duration)

    #선생님처럼 체이닝을 잘 걸어야 되는데~~ 
    element = browser.find_element(By.CSS_SELECTOR, "ul.AutocompleteList").find_element(
        By.TAG_NAME, "li"
    )
    print("검색결과 li 엘리먼트 찾음")
    #===클릭시 계속 방해 해서 넣어 줬음 
    close_ad()
    
    #검색했을 때 첫번째 엘리먼트를 클릭하겠다! 세팅 
    #왜 js로 했냐면 위에 덮어져 있으면 클릭이 안되서 js 넣었음(라디오, 체크박스)
    browser.execute_script("arguments[0].click()", element)
    print("검색결과 li 엘리먼트 클릭")
    time.sleep(loading_duration)

    close_ad()

    time.sleep(loading_duration)
    
    #//div 어딘가의 디브중에서 클래스명이 DayPicker-Caption-Wide을 포함하고있는 엘리먼트 찾아와 
    # element = browser.find_element(
    #     By.XPATH, '//div[contains(@class, "DayPicker-Caption-Wide")]'
    # )
    
    #한줄 씩 요일이 나열(화면상에서는 다른 month가 나타나지 않음)
    #======월 추출하기======→ 업데이트: 연도 추가
    #왜 이렇게 썼냐면 2개라도 첫번째 엘리먼트를 가져오니까 이렇게 사용 
    
    #====년 추출======
    # 연도를 보고 클릭수 아래와 같이 추가 
    # (이렇게 하면 년도도 맞출 수 있다.) 
    # (12-6)+1 (1월 출발 +2하면 이월출발)
    #연도 비교(2023==2024) 한 후 클릭처리

    element = browser.find_element(By.CSS_SELECTOR, "div.DayPicker-Caption-Wide")

    #출발 월, 도착 월, 데이트피커의 월 
    departure_month = int(departure_date[5:7])
    return_month = int(return_date[5:7])
    datepicker_month = int(element.text[6:-1])

#==출발날짜와 보고있는 날짜를 비교하기 위한 변수(6-6이면 0)
    month_difference_1 = 0
    month_difference_2 = 0
    # 7-9
    #큰일 났네ㅋㅋ 이해가 안되는데 ㅋㅋㅋㅋㅋ 

#==클릭을 몇번 할지(도착월이 현재일고 나중일 수도 있어서 )
#7>6: m1=7-6
    # 이때 한번 클릭 값이 m1에 저장 (클릭 1번 함)
    if departure_month > datepicker_month:
        month_difference_1 = departure_month - datepicker_month
#9>6: m2=9-6 ===총 3번 클릭 === (클릭안해서 아직도 6월) 그래서 m2가 3이라는 최종 숫자를 얻게됨 
    if return_month > datepicker_month:
        month_difference_2 = return_month - datepicker_month
#1!=0: 버튼을 누르시오 (출발하는 달과 다르다 →***클릭이 필요함*** 그래서 화살표 버튼 찾으러 감)
    if month_difference_1 != 0:
        element = browser.find_element(
            By.CSS_SELECTOR, 'span[data-selenium="calendar-next-month-button"]'
        )
        #출발 날짜를 클릭하기 위한 for 
        for i in range(month_difference_1):
            close_ad()
            browser.execute_script("arguments[0].click()", element)
            time.sleep(loading_duration)
    #출발월이 정해져서 날짜를 클릭함 
    element = browser.find_element(
        By.CSS_SELECTOR, f'span[data-selenium-date="{departure_date}"]'
    )
    print(f"{departure_date} 엘리먼트 찾음")
    close_ad()
    browser.execute_script("arguments[0].click()", element)
    print(f"{departure_date} 엘리먼트 클릭")
    
    #위에 for문에서 m1이 같지 않다면 
    if month_difference_1 != month_difference_2:
        element = browser.find_element(
            #왜 또 썼냐면 위에 클릭해서 페이지가 변해서 다시 한번 찾아줬음 
            By.CSS_SELECTOR, 'span[data-selenium="calendar-next-month-button"]'
        )
        # 여기서 -를 통해서 클릭을 할 수 있게 만듬 
        for i in range(month_difference_2 - month_difference_1):
            browser.execute_script("arguments[0].click()", element)
            time.sleep(loading_duration)

    element = browser.find_element(
        By.CSS_SELECTOR, f'span[data-selenium-date="{return_date}"]'
    )
    # 객실, 성인, 아동 클릭 할꺼라면 클릭 후 세팅 변수랑 비교해서(if) 검색버튼 눌러야 함 
    # html block(벽), inline block(벽돌), inline() 왜 그렇게 넣었을까?(여기는 버튼안에 div를 넣었거든ㅋㅋ 나나 할 실수를 했구만 ㅋㅋㅋ)
    print(f"{return_date} 엘리먼트 찾음")
    close_ad()
    browser.execute_script("arguments[0].click()", element)
    print(f"{return_date} 엘리먼트 클릭")

    element = browser.find_element(
        By.CSS_SELECTOR, 'button[data-element-name="search-button"]'
    )
    print("검색 버튼 엘리먼트 찾음")
    close_ad()
    browser.execute_script("arguments[0].click()", element)
    print("검색 버튼 엘리먼트 클릭")
    time.sleep(loading_duration * 3)

    close_ad()

#새로운 탭이 열렸을 때 이동하는 코드 
#만약에 원도우 핸들러 랭스가 2가 아니면 x, 2라면 새창이 떴으니까 이동
    if len(browser.window_handles) == 2:
        #[0]:은 origin 이동해서[1] 
        browser.switch_to.window(browser.window_handles[1])

    time.sleep(loading_duration * 3)

    old_height = browser.execute_script("return document.documentElement.scrollHeight")
    scroll_y = 800
    number = 0

#그러면 나는 페이지 다운할려면 저기서 그냥 다운만 세팅해 주면 되나?? 
    while True:
        number += 1
        print(f"스크롤 다운 {number}회차")
        print("이전 웹문서 높이(px)", old_height)

#천천히 스크롤 내리는 방식 
#지금까지는 find_all로 모두 찾기 방식 사용 그러나 여기서는 그렇게 할 수 없음
#이전에는 로케이션 ["y"] 값 추출했음 
#5번 스크롤 내릴거라 5 해 줬음 (스크롤 높이는 본인 모니터에 맞게 세팅 필요)
#웹의 특성마다 다르기 때문에 웹을 분석하고 적용하자 
        for i in range(5):
            browser.execute_script("window.scrollTo(0, arguments[0])", scroll_y)
            browser.execute_script("window.scrollTo(0, arguments[0])", scroll_y - 200)
            scroll_y += 800
            time.sleep(1)

        new_height = browser.execute_script(
            "return document.documentElement.scrollHeight"
        )

        if new_height == old_height:
            print("############## 스크롤 작업이 완료되었습니다. ##############")
            break

        old_height = new_height


except Exception as e:
    raise e
#트라이문이 엄청 긴 형태 → raise: 에러나면 그냥 코드 멈추고 콘솔에 찍기

# 숩객체 만들었다면 브라우저 종료를 해주기 → 다음페이지가 있드면 브라우저 종료하면 안돼!!! 
soup = BeautifulSoup(browser.page_source, "html.parser")
browser.quit()
elements = soup.find_all("ol", attrs={"class": "hotel-list-container"})
#==이렇게 말고 find_all로 li hotel-item으로 가져와도 상관없음 (많은 li가 다 찾아졌음)

# print(len(elements))

#이 방법을 알려주신 이유는 li가 특징이 없는 형태도 있어서 보여 주셨음 
for element in elements:
    hotels = element.find_all("li", attrs={"data-selenium": "hotel-item"})

    print(len(hotels))

    for hotel in hotels:
        hotel_name = (
            hotel.find("h3", attrs={"data-selenium": "hotel-name"}).get_text().strip()
        )
        print(hotel_name)

# 위와 같은 버전 
# item_list=soup.select('li[data-selenium="hotel-item"]')
# for i in item_list:
#     hotels = i.find("h3", attrs={"data-selenium": "hotel-name"}).get_text().strip()
#     print(hotels)

