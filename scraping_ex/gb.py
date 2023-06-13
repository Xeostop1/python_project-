from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
import pandas as pd


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent={}".format(user_agent))
browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
browser.maximize_window()

#####################################

# search_keyword1 = "gaming"
# search_keyword2 = "mouse"
# search_pages = 1

max_height = 5000
loading_duration = 5

##########################

# ----- 작업 순서 -----
# 1. 웹 문서 접속 
# 2. 전체 페이지에서 제품별 링크 긁어오기 (bs4 이용) - 다음 영화 참고
# 2-1. 스폰서 제품은 제외하기 - 구글 if 문 참고 
# 3. 각 제품 별 리뷰 긁어오기 
# 3-1. 각 제품 클릭 
# 3-2. See all reviews 찾아서 클릭하기 (나라별 상관없이 전부 같은 링크임)
# 3-3. 셀레니움으로 next page 찾아서 클릭시켜서 bs4로 리뷰 추출
# 4. 판다스를 이용해 제품을 시트 별로 저장 (마지막에 해도 될 듯)

##########################

# 1~2. 웹 문서 접속 후 제품별 링크 가져오기 

product_urls = []

# for search_page in range(search_pages) : 
#     page_number = search_page + 1
#     url = f"https://www.amazon.com/s?k={search_keyword1}+{search_keyword2}&page={page_number}"
#     browser.get(url)
#     time.sleep(loading_duration)
#     soup = BeautifulSoup(browser.page_source, "lxml")
    
#     products = soup.find_all("div", attrs={"class":"sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16"})
    
#     for product in products:
#         link = product.find("a", attrs={"class":"a-link-normal s-no-outline"})["href"]
#         product_url = "https://www.amazon.com" + link
#         product_urls.append(product_url)
        
#     print(f"{page_number}번째 페이지 작동 중, 제품 링크 {len(product_urls)}개를 가져왔습니다.")

# 3-1~2. 각 제품 링크 접속 후 리뷰 페이지 들어가기 
#############################
# BS4로 리뷰 한 페이지 긁어서 판다스 데이터프레임에 저장하는 함수
def extract_reviews(soup, df_reviews):
    personal_reviews = soup.select("div.a-section.review.aok-relative")
    for idx, personal_review in enumerate(personal_reviews):
        name_personal_review = personal_review.select_one("span.a-profile-name").get_text(strip=True)
        star_personal_review = personal_review.select_one("span.a-icon-alt").get_text(strip=True)[:3]
        title_personal_review = personal_review.select_one("a.a-size-base.a-link-normal.review-title.a-color-base.review-title-content.a-text-bold").get_text(strip=True)
        date_personal_review = personal_review.select_one("span.a-size-base.a-color-secondary.review-date").get_text(strip=True)
        content_personal_review = personal_review.select_one("span.a-size-base.review-text.review-text-content").get_text(strip=True)

        df_reviews = df_reviews.append({
            'Name': name_personal_review,
            'Star': star_personal_review,
            'Title': title_personal_review,
            'Date': date_personal_review,
            'Content': content_personal_review
        }, ignore_index=True)
                
    first_index = max(len(df_reviews) - 10, 0)
    last_index = len(df_reviews) - 1
    if not df_reviews.empty:
        print(f"{len(df_reviews)}개의 리뷰 추출 완료")
        if len(df_reviews) >= 10:
            print(f"첫 번째 이름 : {df_reviews['Name'].iloc[first_index]}\n마지막 이름 : {df_reviews['Name'].iloc[last_index]}")
        else:
            print("리뷰가 10개 미만입니다.")
    else:
        print("리뷰가 존재하지 않습니다.")
    time.sleep(loading_duration)

############################# 
# 모든 리뷰 보기 페이지 xpath
see_all_reviews_button_xpath = "//a[contains(@class, 'a-link-emphasis') and contains(@class, 'a-text-bold')]"

# 판다스로 빈 엑셀 파일 만들기 
writer = pd.ExcelWriter('amazon_search_result.xlsx', engine='xlsxwriter')
# 판다스로 빈 데이터프레임 생성
df_product_info = pd.DataFrame(columns=['Product Title', 'Price'])
df_reviews = pd.DataFrame(columns=['Name', 'Star', 'Title', 'Date', 'Content'])

#############################

url = "https://www.amazon.com/Razer-Basilisk-Customizable-Wireless-Gaming/dp/B0BD3C6C65/ref=sr_1_2?crid=3FTLS53ZGQUX2&keywords=gaming+mouse+razer+basilisk+v3&qid=1686571962&sprefix=gaming+mouse+razer%2Caps%2C422&sr=8-2"
browser.get(url)
time.sleep(0.5)
soup = BeautifulSoup(browser.page_source, "lxml")

each_product_title = soup.select_one("span.a-size-large.product-title-word-break").get_text(strip=True)
each_product_price = soup.select_one("span.apexPriceToPay").select_one("span.a-offscreen").get_text(strip=True)
print(each_product_title, each_product_price)

df_product_info = df_product_info.append({
    'Product Title': each_product_title,
    'Price': each_product_price,
}, ignore_index=True)

try:
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, see_all_reviews_button_xpath))
    )
    review_button = browser.find_element(By.XPATH, see_all_reviews_button_xpath)
    print("See all reviews 버튼 발견")
    review_button.click()
    print("See all reviews 버튼 클릭")
    time.sleep(loading_duration)
except Exception as e:
    print("See all reviews 버튼 찾는 도중 에러 발생")
    print(e)

while True:     
    soup = BeautifulSoup(browser.page_source, "lxml")
    extract_reviews(soup, df_reviews)
#     try:
#         next_review_button = browser.find_element(By.CLASS_NAME, "a-last")
#         print("Next page 버튼 발견")
#         next_review_button.click()
#         print("Next page 버튼 클릭")
#         time.sleep(loading_duration)
#     except NoSuchElementException as Noex:
#         print("Next page 버튼을 찾을 수 없습니다. 리뷰 수집 종료")
#         print(Noex)
#         break
#     except Exception as ex:
#         print("Next page 버튼 찾는 도중 에러 발생")
#         print(ex)
    
# 시트 생성 후 저장
    df_product_info.to_excel(writer, sheet_name=each_product_title[:16], index=False, startrow=1)           
    df_reviews.to_excel(writer, sheet_name=each_product_title[:16], index=False, startrow=3)
    break

# 데이터프레임 초기화 (새로운 시트에 다음 제품 저장하기 위해 데이터프레임 리셋)
# df_product_info = pd.DataFrame(columns=['Product Title', 'Price'])
# df_reviews = pd.DataFrame(columns=['Name', 'Star', 'Title', 'Date', 'Content'])

        
writer.save() 