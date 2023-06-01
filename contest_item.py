#======요즘것들 공모전 스크래퍼===================
# from requests import get
from bs4 import BeautifulSoup
#from 폴더이름.파일명 import 함수명
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


for page in range(pages):
    page_num=page+1
    url=f"https://section.cafe.naver.com/ca-fe/home/search/articles?q={keyword}&pr=7&ps={start_date}&pe={end_date}"
    browser.get(url)
    time.sleep(3)
    soup= BeautifulSoup(browser.page_source, "html.parser")
    item_list=soup.find("ul", class_="ArticleList").find_all("div", class_="detail_area")
    
    count=0
    for i in item_list:
        count+=1
        title=i.find("a", class_="item_subject").get_text().strip()
        description=i.find("p",class_="item_content").get_text().strip()
        print(f"{count} 제목: {title} / 설명: {description}")
    



#======페이지카운터 함수=======
def get_page_counter():
  #옵션세팅
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)

  base_url = "https://allforyoung.com/posts/contest"

  response = browser.get(f"{base_url}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  page_num = soup.find("div", class_="cwUyxs")
  if page_num == None:
    return 1
  page_ul = page_num.find("ul", class_="pagination__Flex-sc-u22h11-0")
  page_list = page_num.find_all("li")
  print(page_list)
  count = len(page_list)
  if count >= 5:
    return 5
  else:
    return count


#====================클론코딩================================
# def plus(a="num writeing plese",b="num writeing plese"):
#     print(a)
#     print(a+b)

# def minus(a="num writeing plese",b="num writeing plese"):
#     print(a-b)

# def mul(a="num writeing plese",b="num writeing plese"):
#   print(a)
#   print(a*b)

# def de(a="num writeing plese",b="num writeing plese"):
#     print(b)
#     print(a/b)

#진짜 너무 편하네 정말로!
#리스트에 있는 인덱스를 바로 숫자로 변화 1부터 시작 명심
# index_num=[1,2,3]
# f,s,t=index_num
# print(f,s,t)

# from requests import get
# from bs4 import BeautifulSoup
# #from 폴더이름.파일명 import 함수명
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from extractors.wwr import extract_wwr_jobs
# from extractors.indeed import extract_indeed_jobs

# #여기는 replit때문에 작성하는 파트
# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# browser = webdriver.Chrome(options=options)

# #=====유저 직접검색=======
# keyword = input("what do you want search for?")
# indeed = extract_indeed_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# #2개의 함수에서 리턴받은 리스트 합치기(+사용)
# jobs = indeed + wwr
# #====검색어.csv open으로 만들기(2번째 파라미터로 "w" 넣기)
# #open: 열거나 만들고 싶은 파일이름을 적어서 바로 실행
# file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
# #파일세팅 ,로 구분
# file.write("Position, Company, Location, URL\n")
# #리스트 각각 아이템 넣기
# for job in jobs:
#   file.write(
#     f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")
# file.close()

# websie = ("google.com", "airbnb.com", "youtube.com", "naver.com", "daum.net",
#           "httpstat.us/502", "httpstat.us/404", "httpstat.us/300",
#           "httpstat.us/200", "httpstat.us/101")

#리퀘스트 결과를 담는 딕셔널리
#wwr사이트 스크랩퍼
# jobs=extract_wwr_jobs("python")
# #리턴값밖에 없어서 변수에 넣고 프린트 해야돼 정신차려
# print(jobs)

# for site in websie:
#   if not site.startswith("https://"):
#     site = f"https://{site}"
#     response = get(site)
#     c_num = response.status_code
#     responseCode(c_num)

#    print(response.status_code)
#   if response.status_code==successful_c:
#      res[site]="OK"
#   else:
#     res[site]="FAILED"
#print(res)

# #======페이지카운터 함수=======
# def get_page_counter(job_name):
#   #옵션세팅
#   options = Options()
#   options.add_argument("--no-sandbox")
#   options.add_argument("--disable-dev-shm-usage")
#   browser = webdriver.Chrome(options=options)

#   base_url = "https://kr.indeed.com/jobs?q="

#   response = browser.get(f"{base_url}{job_name}")
#   # c_num = response.status_code
#   # responseCode(base_url=base_url, num=c_num)
#   # text는 못가지고 오고, page_source 가져오는 것 확인
#   # 왜 response로 가져오지 않는건지는 확인 불가능
#   soup = BeautifulSoup(browser.page_source, "html.parser")
#   navi = soup.find("nav", role="navigation")
#   if navi == None:
#     #페이지 수가 1개 이다 그래서 리턴1
#     return 1
#   page_list = navi.find_all("div", recursive=False)
#   count = len(page_list)
#   #5개 보다 많아서 페이지에서 5가 max가 5단위로 끊고, 아니면 렝스 만큼 실행
#   if count >= 5:
#     return 5
#   else:
#     return count

# #=======indeend 스크래퍼========
# def extract_indeed(job_name):
#   #====페이지추가=====
#   pages = get_page_counter(job_name)
#   print("chechk", pages, "페이지")
#   results = []
#   #페이지 만큼 range로 배열 만들어서 돌리기(for루프)
#   for page in range(pages):
#     #====옵션세팅=====(for loop안에 넣어줘야 페이지마다 세팅이 되나봐!! 에러 찾았다)
#     options = Options()
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     browser = webdriver.Chrome(options=options)
#     #===대기시간 추가=====(굳이 안해도 괜찮음)
#     # browser.implicitly_wait(20)

#     #나는 이렇게 했는데 없어도 q쿼리 이후에는 없어도 되나봐
#     base_url = "https://kr.indeed.com/jobs"
#     final_url = f"{base_url}?q={job_name}&start{page*10}"
#     print("리퀘스팅", final_url)
#     #startpage(current*10) 추가 ineed가 start가 그렇게 생겨먹어서
#     browser.get(final_url)
#     #셀레니움에서 파서 연결
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     #중복 클래스명 찾고 (여기는 1개만 있어서 find 사용!! 잘보고 써야돼)
#     job_list = soup.find("ul", class_="jobsearch-ResultsList")
#     #거기서 all로 모든 요소 가지고 오기
#     jobs = job_list.find_all("li", recursive=False)
#     #recursive 매개변수는 불리언. 문서에서 얼마나 깊이 찾아 들어가고 싶은지를 지정.
#     #recursive가 True이면 findAll 함수는 매개변수에 일치하는 태그를 찾아 자식, 자식의 자식을 검색. false이면 문서의 최상위 태그만 검색.
#     #내가 생각한 데로 [0]이면 한개 li밖에 못가져 올꺼야!

#     #모든 데이터를 가지고 올때 mosaic를 조심하자 → None으로 해결(있는데 없는거라서)
#     for job in jobs:
#       zone = job.find("div", class_="mosaic-zone")
#       #모자이크div를 찾고 내용이 빈(none) 찾기
#       if zone == None:
#         #쿼리셀렉터 처럼 사용가능함
#         #select_one: 페이지 소스가 바뀌어서 select가 미사용
#         anchor = job.select_one("h2 a", class_="jobTitle")
#         if anchor != None:
#           title = anchor["aria-label"]
#           link = anchor["href"]
#         company = job.find("span", class_="companyName")
#         location = job.find("div", class_="companyLocation")
#         job_data = {
#           # 링크는 f 문자지정해줘야함(상대경로라서 c:~~ 이런게 생략된것 처럼)
#           "link": f"https://kr.indeed.com{link}",
#           "company": company.string,
#           "location": location.string,
#           #왜 타이틀만 스트링화를 안해주는거지??? 이해가 안간다!이건 이미 str 상태라서 그런가봐
#           #나머지는 str 상태가 아니라(type(태그상태임)) 세팅해준거고 나처럼 title.string하면
#           #2번 작업한거라 세팅이 안됨
#           "position": title
#         }
#         results.append(job_data)
#     # 결과물 출력
#     # for i in results:
#     #   print(i)
#     #   print("========================")
#   return results

# jobs = extract_indeed("react")
# print(len(jobs))

# #=======접속 코드 함수========
# def responseCode(num, base_url):
#   res = {}
#   server_e = 500
#   client_e = 400
#   redirection_c = 300
#   successful_c = 200
#   info_r_c = 100
#   if num >= server_e:
#     res[base_url] = "server_error", num
#   elif num >= client_e:
#     res[base_url] = "client_error", num
#   elif num >= redirection_c:
#     res[base_url] = "redirection", num
#   elif num >= successful_c:
#     res[base_url] = "successful", num
#   elif num >= info_r_c:
#     res[base_url] = "info_r", num
#   print(res)
#   return res

#나는 이렇게 했는데 없어도 q쿼리 이후에는 없어도 되나봐
# base_url = "https://kr.indeed.com/jobs?q="
# keyword = "python"
# # #겟메서드로 쿼리 보내기
# # response=get(f"{base_url}{keyword}")
# # c_num = response.status_code
# # responseCode(base_url=base_url,num=c_num)

# #봇때문에 결국은 셀레니움을 배우게 된다~~~셀레니움 파트
# #리퀘스트 미사용: 셀레니움은 직접 브라우저를 여는 거라서(사실 봇이라 차단 당했음)
# #여기는 replit때문에 작성하는 파트
# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# browser = webdriver.Chrome(options=options)
# browser.get(f"{base_url}{keyword}")
# # browser.get("https://kr.indeed.com/jobs?q=python")
# # print(browser.page_source)
# #셀레니움에서 파서 연결
# soup = BeautifulSoup(browser.page_source, "html.parser")
# results = []
# #중복 클래스명 찾고 (여기는 1개만 있어서 find 사용!! 잘보고 써야돼)
# job_list = soup.find("ul", class_="jobsearch-ResultsList")
# #거기서 all로 모든 요소 가지고 오기
# jobs = job_list.find_all("li", recursive=False)
# #recursive 매개변수는 불리언. 문서에서 얼마나 깊이 찾아 들어가고 싶은지를 지정.
# #recursive가 True이면 findAll 함수는 매개변수에 일치하는 태그를 찾아 자식, 자식의 자식을 검색. false이면 문서의 최상위 태그만 검색.
# #내가 생각한 데로 [0]이면 한개 li밖에 못가져 올꺼야!

# #모든 데이터를 가지고 올때 mosaic를 조심하자 → None으로 해결(있는데 없는거라서)
# for job in jobs:
#   zone = job.find("div", class_="mosaic-zone")
#   #모자이크div를 찾고 내용이 빈(none) 찾기
#   if zone == None:
#     #쿼리셀렉터 처럼 사용가능함
#     #select_one: 페이지 소스가 바뀌어서 select가 미사용
#     anchor = job.select_one("h2 a", class_="jobTitle")
#     if anchor != None:
#       title = anchor["aria-label"]
#       link = anchor["href"]
#     company = job.find("span", class_="companyName")
#     location = job.find("div", class_="companyLocation")
#     job_data = {
#       # 링크는 f 문자지정해줘야함(상대경로라서 c:~~ 이런게 생략된것 처럼)
#       "link": f"https://kr.indeed.com{link}",
#       "company": company.string,
#       "location": location.string,
#       #왜 타이틀만 스트링화를 안해주는거지??? 이해가 안간다!이건 이미 str 상태라서 그런가봐
#       #나머지는 str 상태가 아니라(type(태그상태임)) 세팅해준거고 나처럼 title.string하면
#       #2번 작업한거라 세팅이 안됨
#       "position": title
#     }
#     results.append(job_data)
# for i in results:
#   print(i)
#   print("========================")

#기존ID로 찾는 방법
# print("job list")
# h2=job.find("h2",class_="jobTitle")
# a=h2.find("a")

# base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
# # 검색하는 단어
# search_term = "python"
# response = get(f"{base_url}{search_term}")
# c_num = response.status_code
# # print(response.text)
# responseCode(c_num)
# soup=BeautifulSoup(response.text,"html.parser")
# #find_all() 쿼리로 찾아오기
# jobs=soup.find_all('section', class_="jobs")
# #최종결과저장 딕셔너리
# results=[]
# for job_s in jobs:
#   # job_post=job_s.find_all("li", class_="feature")
#   #위와 같은 결과 쿼리가 없을 때 사용가능함
#   job_post=job_s.find_all("li")
#   job_post.pop(-1)
#   for post in job_post:
#       anchors=post.find_all("a")
#       anchor=anchors[1]
#     #엑셀 cvs로 저장
#       link=anchor["href"]
#     #인덱스에서 바로 변수 지정(리스트의 길이를 알때만 사용)
#       company, kind, region =anchor.find_all("span", class_="company")
#       title=anchor.find('span', class_="title")
#     #태그없이 str 저장 .string
#       # print(company.string, kind.string, region.string, title.string)
#       # print("==================\n==================")
#     #for에서 딕셔너리 형태로 저장
#       job_data={
#         "company": company.string,
#         #"kind":kind.string,
#         "region": region.string,
#         "position":title.string
#       }
#       results.append(job_data)
# for i in results:
#     print(i)
#     print("================")
