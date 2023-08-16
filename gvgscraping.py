from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup, NavigableString
import time


user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url="https://www.gvg.co.kr/#3"
browser.get(url)
time.sleep(3)
soup=BeautifulSoup(browser.page_source, "html.parser")
#근데 왜 체이닝이 안되지?? 도대체가 이렇게 드럽게 써야된다고? 환장하겠네
h_title_warp=soup.select_one("div#div_maincontainer")
h_title_warp2=h_title_warp.select_one("ul.ul_defaultcontainer")
#헤더타이틀
h_title=h_title_warp2.select_one("div.Msticker>p.title").get_text().strip()
#브랜드
brand=h_title_warp.select_one("div.p_pcsbrand").get_text().strip()
#설명
# description_wrap=h_title_warp2.select_one("div.p_pcsremark")
div_element = soup.select_one("div.p_pcsremark")
description=h_title_warp2.select_one("div.p_pcsremark>span").get_text().strip()

text_node=text_nodes = [node for node in div_element.children if isinstance(node, NavigableString) and node.string.strip() != ""]

if len(text_nodes) > 0:
    #공백제거
    text_node = text_nodes[0].strip()
    print("Found desired text:", text_node)
else:
    print("Failed to find desired text")