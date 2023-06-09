from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent={}".format(user_agent))

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()

url = "https://www.agoda.com/ko-kr/activities/search?cityId=9395&site_id=1891463&tag=45b17d1d-e0b0-fe2a-ce90-5513829d856b&device=c&network=g&adid=576932895507&rand=7543741664118068119&expid=&adpos=&aud=kwd-6927948326&gclid=CjwKCAjw1YCkBhAOEiwA5aN4AdQEwSD6BXhCkj10_-dpDCY-gf7PtUkimdcyeZq6m_rehw1vQA-ykxoCYjcQAvD_BwE&checkIn=2023-01-02&checkOut=2023-01-04&adults=1&rooms=1&pslc=1&currency=KRW"
browser.get(url)
time.sleep(10)

element = browser.find_element(By.ID, "value")
print(element)
element.send_keys(Keys.RETURN)
time.sleep(2)
button_element = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div/input')
button_element.clear()
button_element.send_keys('방콕')
button_element.send_keys(Keys.RETURN)

time.sleep(5)

print("Clicked")

page_number = 0

while True:
    page_number += 1
    print("Current Page:", page_number)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    info_blocks = soup.find_all("div", attrs={"class": "sc-kOPcWz bAGWai"})

    for idx, info_block in enumerate(info_blocks):
        festival_title = info_block.find_all("h3", attrs={"data-element-name": "activities-card-title"})
        festival_satisfaction = info_block.select_one("span", attrs={"class": "sc-kpDqfm sc-dAlyuH bredbv hjATSZ"})

        if festival_satisfaction is None:
            festival_satisfaction = "No satisfaction information"
        else:
            festival_satisfaction = festival_satisfaction['style'][6:-1]

        print(f"Data Number: {idx + 1}")
        print(f"Data Title: {festival_title}")
        print(f"Data Satisfaction: {festival_satisfaction}")

    print(f"Page {page_number} extraction complete")

    next_button = browser.find_element(By.CSS_SELECTOR, "button[data-element-name='activities-pagination-next-btn']")
    if next_button.get_attribute("disabled"):
        break

    next_button.click()
    time.sleep(10)

browser.quit()
