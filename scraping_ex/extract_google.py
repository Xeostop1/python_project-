from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"

options=webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument(f"user-agent={user_agent}")

browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

keyword="담꾹"
url=f"https://www.google.com/search?q={keyword}&newwindow=1&sxsrf=APwXEddNpqrGeB5IZ2AkCJExq1ozP0P2AQ%3A1685662603965&ei=iyt5ZKnGOoaSseMPg6i6iA4&ved=0ahUKEwjpt-HFnqP_AhUGSWwGHQOUDuEQ4dUDCBA&uact=5&oq=%EB%8B%B4%EA%BE%B9&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCMQigUQJzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECCMQJzoLCAAQgAQQsQMQgwE6CwguEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoICAAQgAQQsQM6BAgAEANKBAhBGABQAFjXB2DuCWgAcAF4AIABXIgBmwSSAQE2mAEAoAEBwAEB&sclient=gws-wiz-serp#ip=1"
browser.get(url)
time.sleep(3)

soup=BeautifulSoup(browser.page_source, "html.parser")
title_list=soup.select("div.MjjYud")

for i, item in enumerate(title_list):
    titles=item.select_one("h3.LC20lb.MBeuO.DKV0Md")
    des=item.select_one("span.MUxGbd.wuQ4Ob.WZ8Tjf:nth-child(2)")
    if titles:
        print(titles.get_text().strip())
        print(des.string().strip())
    else:
       print("None Error")
       continue
