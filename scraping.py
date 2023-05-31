from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(r'C:\Users\coms\Desktop\python_ex\python_project-\scraping_yanolja\chromedriver.exe',
chrome_options=chrome_options)
driver.set_window_size(1024,800)
driver.implicitly_wait(3)

#======스크롤링======
#셀레니움 스크롤 끝까지 내려도 계속 내리는 페이지라면

prev_height = driver.excute_script("return document. body.scrollHeight")
import time
while True:
	#첫번째로 스크롤 내리기
	driver.excute_script("window.scrollTo(0,document.body.scrollHeight)")

	#시간대기
	time.sleep(2)

	#현재높이 저장
	current_height = driver.excute_script("return document. body.scrollHeight")
	#현재높이와 끝의 높이가 끝이면 탈출
	if current_height == prev_height:
		break
	#업데이트해줘서 끝낼 수 있도록
	prev_height == current_height



def extract_yanolja():
    result = []
    #셀레니움 세팅
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(r'C:\Users\coms\Desktop\python_ex\python_project-\scraping_yanolja\chromedriver.exe',
    chrome_options=chrome_options)
    driver.set_window_size(1024,800)
    driver.implicitly_wait(3)
    
    # url세팅 
    base_url = "https://www.yanolja.com/leisure/list?mediumcat=10120006"
    print("리퀘스팅", base_url)
    driver.get(base_url)
    #셀레니움에서 파서 연결
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # title_list=soup.select("div",class_="LeisureListItem_body__1iNjJ")
    name=soup.find_all("p",class_="LeisureListItem_title__U-d8s")
    price=soup.find_all("span", class_="LeisurePriceDiscount_amount__19qBa")
    items={}
    for i in name:
        for j in price:
            items={
            "name":i.string,
            "price":j.string
            }    
        result.append(items)
    return result
            
        
    

    
    # for i in title_list:
    #     title=soup.find("p",class_="LeisureListItem_title__U-d8s")
    #     pirce=soup.find("span",class_="LeisurePriceDiscount_amount__19qBa")
    #     items={
    #         "title":title.text,
    #         "pirce":pirce.text
    #     }
    #     # print(items)
    # results.append(items)
    # return results


res=extract_yanolja()
print(res)

