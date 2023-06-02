#if
#====연습문제1 5/23======
# 17시 이후면 퇴근할 시간입니다를 출력하고 17이전이면 아직 근무 시간입니다 출력 
time=14
leave_tiem=17
if time>=leave_tiem:
    print("퇴근할 시간입니다")
elif time<leave_tiem:
    print("근무시간 입니다")
    #else로 사용하여도 괜찮음 


#====연습문제2 5/23======
# 9시 이상 12 미만 오전
# 12이상 ~13 이하 점심 
# 13초과 17이하 오후근무
# 이외의 시간 근무시간 외를 출력하는 if
time=11
if 9<=time<12:
    print("오전")
elif 12<=time<=13:
    print("점심")
elif 13<=time<=17:
    print("오후")
else:
    print("근무시간 외")

#======in, not in========
a=["안녕", "하세요"]
if "안녕" in a:
    print("안녕하세요")
    # a의 요소에 안에 안녕이 있으면 실행 
elif "hello" not in a:
    print("없어요 ")
    # a의 요소에 안에 안녕이 없으면 실행
    
#=======pass=========
# continue와 같은 의미 pass 써주면 됨 

#=====줄여서 사용 :없이 사용함 3항표현식과 똑같네======
# grade="High Distinction" if x>90 else "pass"


#====연습문제3 5/23======
# 주민번호 중 성별, 생년월일 추출 아래 예시와 같이 출력
# 1번
# 생년월일: 88년 12월 25일생 
# 성별: 남자

RRN1="881225-1234567"
RRN2="880312-2234567"

def gender_check(code):
    #선생님 변수명 user_year
    #인트값으로 하거나 둘다 str로 변경해야 함! 
    gender=int(code[7])
    male=1
    year=code[:2]
    day=code[2:4]
    month=code[4:6]
    
    print("1번")
    print(f"생년월일{year}년 {day}월 {month}일생")
    if gender==male:
        print("성별: 남자") 
    else:
        print("성별: 여자")
    
gender_check(RRN1)
    
    
#====연습문제5 5/23======
# 변수 내 every라는 단어가 있다면 nice to meet you all 문장을 출력하는 if 
# afternoon 이라는 단어가 없다면 it's 9 in the morning 출력 
greeting="Good morning everyone!"

if "every" in greeting:
    print("nice to meet you all")
if "afternoon" not in greeting:
    print("it's 9 in the morning")
    
#====연습문제6 5/23======
# 조건부 표현식을 이용 score가 65이상일 때 변수 grade에 pass 대입, 
# 아닐 때 변수 grade fail 대입하는 조건문 작성
score=80
grade=""

#둘중에 한개를 무조건 실행하기 때문에
grade="Pass" if score >=65 else "Fail"

if score>=65:
    grade="pass"
else:
    grade="Fail"

print(grade)
    
