from bs4 import BeautifulSoup
import requests
#정규표현식 import 레귤러익스텐션이던가
import re


url= "http://www.yes24.com/24/category/bestseller"
res= requests.get(url)
soup=BeautifulSoup(res.text, "html.parser")
#체이닝으로 연결
#ol.finld_all("p",{attrs="class=속성명"})
#추출할 범위를 꼭 상정하고 스크래핑을 하자 

#리스트형태로 저장(soup객체라서 soup메서드 사용 )
titles=soup.find("div",attrs={"id":"bestList"}).ol.find_all("p", attrs={"class":"copy"})
author=soup.find("div",attrs={"id":"bestList"}).ol.find_all("p", attrs={"class":"aupu"})
book_names=soup.find("div",attrs={"id":"bestList"}).ol.find_all("li", attrs={"class":re.compile("num")})


#도서책 find_next_sliling 사용 
# book_names=soup.find("div",attrs={"id":"bestList"}).ol.find("li > p:nth-child(3)")
# num을 통한 정규표현식 import해서 가져오기 
# book_names=soup.find("div",attrs={"id":"bestList"}).ol.find_all("li", attrs={"class":re.compile("num")})
book_names = soup.find("div", attrs={"id":"bestList"}).ol.find_all("li", attrs={"class":re.compile("num")})
# .p.find("p", attrs={"id":"location_0"}).find_next_siblings("p")
print(book_names)

# name=book_names.p.find("p", attrs={"id":"location_0"}).find_next_siblings("p")
#.하면 안에 있는 거니까 

# 리스트라 안에 들어가서 세팅해야 되나봐, 밖에서는 안되넹 이미 불러와 져서 그런가?? 
# 큰 엘리먼트 안에 있어서 그런 듯 li안에 있는 p가 여러개 리스트에 넣어져 있어서 
# for 에서 찾으니까 여러개 한꺼번에 넣을 수 있어서 편하긴 하네
count=0
for i in book_names:
    count+=1
    #다음 형제 찾기
    name=i.find("p", attrs={"class":"image"}).find_next_sibling("p").a.get_text().strip()
    pirce=i.find("p", class_="price").strong.get_text().strip()
    
    print(f"[{count}]","제목:",name,"/ 가격:",pirce)





#그냥 함수를 쓰고 끌어내리면 되나?? 
#그러면 언제까지 내려야 하는데??? 그냥 내린 뒤에 bs4로 스크래핑 하면 되나봐 

#넘버링

# for i in book_name:
#     print(i)
# for i in titles:
#     count+=1
#     #get_text bs4 메서드 text 가져옴, strip()도 이용하여 공백 제거(앞 뒤로)
#     i=i.get_text().strip()
#     #데이터가 없을 경우 사용 None 대비 
#     if i=="":
#         i="###제목없음####"
#     for j in author:
#         j=j.get_text().strip()
#     print(count,i,"저자:",j,"\n")
    
    

