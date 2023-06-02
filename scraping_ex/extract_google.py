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

#구글검색: 날짜 포함, 페이지 추가 검색/ 구글은 자주 바뀜(구조와 패턴은 비슷함)
#===패턴====
#1. 구글은 시작점이 0 +10씩 증가 


browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

keyword="담꾹"
s_date="1/1/2020"
e_date="5/31/2023"
loding_time=2
pages=5

#1.클래스로 g 가져오기 → if에 자식이 있다면 따로 처리 문제는 중복되는 값이 너무 많음 
#2.큰 뎁스에서 다른 엘리먼트가 나온다면 어떻게 처리할 것인가? → 리스트를 가지고 와서 엘리먼트로 넣기 
#g를 가지고 와서 들여쓰기 엘리먼트 구조가 있다면 새로운 리스트에 저장 / 아니면 그냥 저장하기 두개를 어팬드 해서 하나의 리스트결과문 만들기 


# browser.get(url)
# time.sleep(3)

#result_container
final_res=[]

#1for 큰 뎁스 찾기
for i in range(0, pages*10, 10):
    #페이지 위치 파악 숫자(콘솔 확인용으로 좋다!)
    page_num=int(i/10+1)
    url=f"https://www.google.co.kr/search?q={keyword}&newwindow=1&tbs=cdr:1,cd_min:{s_date},cd_max:{e_date}&sxsrf=APwXEdc8HQxd0DyhZaC_SwljfqeRjXBGDg:1685683396570&ei=xHx5ZOemIrC12roPjISH4AQ&start={i}&sa=N&ved=2ahUKEwjnmLmA7KP_AhWwmlYBHQzCAUwQ8tMDegQIBxAI&biw=899&bih=937&dpr=1"
    browser.get(url)
    time.sleep(loding_time)
    #===여기에 튜링테스트 봇 설정 넘어가기 코드 만들기===
    
    
    
    soup=BeautifulSoup(browser.page_source,"html.parser")
    
    #search_list=soup.find("div", id="serch").find_all("div", class_="g") 
    #search_list=soup.find("div", attrs={"id":"search"}).find_all("div", attrs={"class":"g"}) 
    #search results →모든 g클래스 가져오기 안정장치라서 2개 걸어줬음
    search_list=soup.select("div.g")
    print("현재페이지:", page_num)
    print("검색결과 수:", len(search_list))
    print("="*10)

#1-2 for 1분기 들여쓰기 뎁스 내용 추출
    for i in search_list:
        if i.select_one(".d4rhi"):
            sub_list=i.find_all(recursive=False)
            for sub_j in sub_list:
                final_res.append(sub_j)
        else:
            final_res.append(i)


#3 for find를 쓰는 이유가 or로 묶을 수 있기 때문이 find를 사용했음 
for i in final_res:
    title=i.find("h3", attrs={"class": ["LC20lb MBeuO DKV0Md", "LC20lb MBeuO xvfwl"]}).get_text().strip()
    content=i.find("span", class_="MUxGbd wuQ4Ob WZ8Tjf").next_sibling.get_text().strip()
    # content=i.find("span", class_="MUxGbd wuQ4Ob WZ8Tjf").contents[1].get_text().strip()
    date=i.find("span", attrs={"class":"MUxGbd wuQ4Ob WZ8Tjf"}).span.get_text().strip()
    print("제목: ",title)
    print("내용: ",content)
    print("날짜: ",date)
    
    
    



#====seohana 버전=========

# soup=BeautifulSoup(browser.page_source, "html.parser")
# title_list=soup.select("div.MjjYud")

# for i, item in enumerate(title_list):
#     titles=item.select_one("h3.LC20lb.MBeuO.DKV0Md")
#     des=item.select_one("span.MUxGbd.wuQ4Ob.WZ8Tjf:nth-child(2)") 
#     if titles:
#         print(titles.get_text().strip())
#     else:
#        print("None Error")
#        continue
