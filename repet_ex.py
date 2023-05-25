for i in [1,2]:
    print(i)
#===문자열 추출도 가능함=====

#====연습문제1 5/23======
"첫번째 상품은 '사과'입니다와 같은 방식으로 출력 "
# 1.문자열 포맷팅을 이용하지 않고 출력
# 2.문자열 포맷팅을 이용하여 출력(2개)
products=["사과", "오렌지", "파인애플", "포도"]
# for 루프: 1개씩 꺼내서 가능할 때 사용
# 와일 루프: 무한반복(조건을 통해서 확인) 

#선생님은 랭스 대신 num으로 카운터 넣어줬음 

for i,fruit in enumerate(products):
    # print("상품은" +fruit+"입니다")
     print(f"{i+1}상품은 {fruit} 입니다")
    # print("상품은 {} 입니다".format(fruit))
    
    
#====연습문제2 5/23======
# score에 포함된 요소들의 점수에 맞게 1번째 학생의 등급은 __입니다와 같은 방식으로 출력 
# 등급표: 50미만 fail
# 50이상 65미만 pass
# 65이상 75미만 credit
# 75이상 85미만 distioncion
# 85이상    high distioncion
score=[99,80,60,40,67]
grade=""

for i,stu in enumerate(score):
    if stu>=85:
        grade="high distioncion"
    elif 75<=stu<85:
        grade="distioncion"
    elif 65<=stu<75:
        grade="credit"
    elif 50<=stu<65:
        grade="pass"  
    elif 50>stu:
        grade="fail"  
        
    print(f"{i+1}번째 학생의 점수{stu}/등급 {grade}입니다")
    
    
    
# num=0
# for stu in score:
    # num+=1
    # if stu>=85:
        # grade="high distioncion"
    # elif 75<=stu<85:
        # grade="distioncion"
    # elif 65<=stu<75:
        # grade="credit"
    # elif 50<=stu<65:
        # grade="pass"  
    # elif 50>stu:
        # grade="fail" 
    # print(num)
    #왜 안되지???
    # print(f"{score[num]}번째 학생의 점수{stu}/등급 {grade}입니다")
    
#range()연속변수 만들기
# 1개: 0부터 ~n까지
# 2개: n~n2까지
# 3개: n~n2까지 n3 간격만큼 

# range(len())의 갯수만큼 들어감 
sum=0
for i in range(1,11):
    sum+=i
print(sum)

sum2=0
score=[30,50,60,90]

# 와 썸함수도 걍 만들어 났어sum(item)
#enumerate 이거 안써도 되는구나

#for (let i = 0; i < letters.length; i++)랑 같은 방식 
for i in range(len(score)):
    sum2+=score[i]
    print(i)
    # print(score[i])
    
# print(sum2)

#====연습문제1 5/25======
# a를 사용해서 T이면 if실행 a 거짓이면 else a는 참, a는 거짓 문장 출력 
a="abcd"

# a==a
if a:
    print(f"{a}는 참")
else:
    print(f"{a}는 거짓")
    
    
#====연습문제2 5/25======
# ab 조건으로 사용 if  작성 a 참이면 a는 참 b가 참이면 b는 참 ab가 모두 참이 아니면 모두 참이 아님 문장출력
a=0
b=1
if a:
  print(f"{a}는 참")  
elif b:
  print(f"{b}는 참")
elif not a and not b:
  print(f"{a}{b}는 false")
  
  
#====연습문제4 5/25======
# ab 사용하여 a가 b보다 클경우 a는 b보다 크다가 출력되는 if를 작성
a=30
b=20
if a>b:
    print(f"{a}가 {b}보다 크다")

#====연습문제5 5/25======
# 코드수정 에러가 나나???? 안나는데?????
#formating 함수 
a="morning"
b=7
print("It's {} in the {}.".format(b,a))


#====연습문제7 5/25======
# a에 할당된 값이 evening이 아닐 경우 실행되는 if작성 "안녕하세요. 아침입니다" 출력
a="moring"
if a!="evening":
  print("안녕하세요. 아침입니다")
if "evening" not in a:
    print("안녕하세요. 아침입니다")
    
    
#====연습문제8 5/25======
# ab가 모두 참일 때 실행되는 if ab는 모두 참입니다
a="I'm True"
b="I'm also True"

if a and b:
    print(f"{a}와 {b} 모두 참")
    
#====연습문제9 5/25======
# a가 morning 이고 b가 12시 이전일 때 아침입니다. 현재시각은 b 입니다 출력 출력시 포맷함수 사용 시간은 변수  b 이용
a="morning"
b=7
if  a=="morning" and b<12:
    print(f"아침입니다 현재시각은 {b}시 입니다")


#====연습문제10 5/25======
# apple이 있으면 사과를 팔수 있습니다.  orange가 없으면 오렌지는 팔수 없습니다. pineapple있으면 팔수있습니다. if 작성

a=["apple",["kiwi","pineapple"]]

# 이렇게 안되는데??? → 수정필 
# if로 나 따로따로 하셨어
# for i in a:
    # if i in "apple":
        # print("apple 팔수 있습니다")
    # elif i in "orange":
        # print("orange 팔수 없습니다")
    # elif i in "pineapple":
        # print("pineapple 팔수 있습니다")



#====연습문제11 5/25======
# score 60 이상일때  grade에 합격 아니면  불합격 대입 조건문 1줄 작성 후 format()이용하여 당신은 합격 입니다 변수 result에 저장 출력
score=90
grade="합격" if score>=60 else "불합격"
result=f"당신은 {grade}입니다"

# 이렇게는 안된다~~~~~ 3항연산자를 쓰고싶다다다다다다다
# result=if score>60 {grade="합격"} print(f"당신은 {grade} ")else grade= "불합격" print(f"당신은 {grade}입니다")


#====연습문제12 5/25======
# 성별 생년월일 추출 성별확인하여 1,3=남자, 2,4면 여자  조건을 포함
RRN="881225-2234567"
gender_num=int(RRN[7])
if gender_num ==1 or gender_num ==3:
    print(f"생년월일: {RRN[:2]}년 {RRN[2:4]}월 {RRN[4:6]}일")
    print("성별: 남자")
elif gender_num ==2 or gender_num ==4:
    print(f"생년월일: {RRN[:2]}년 {RRN[2:4]}월 {RRN[4:6]}일")
    print("성별: 여자")
    
    
#====연습문제13 5/25======
# a에 알파벳이 문자가 할당되면 문자가 대문자 인지 소문자인지 판별한후 대문자 이면 a는 대문자 입니다. 소문자 이면 소문자 입니다 코드 작성
a="b"
if a.islower():
    print(f"{a}에 값은 소문자 입니다")
elif a.upper():
    print(f"{a}에 값은 대문자 입니다")


#====연습문제14 5/25======
# 13자리 주민번호 마지막 숫자는 유효성 판별을 위해 사용됨, 가장 앞자리 부터 234567892345를 차례로 곱한 뒤 
# 그값을 전부 더한 후 얻은 값을 11로 나누었을때 나머지를 다시 11에서 뺀 값이 번호의 마지막 번호의이
# 이계산법을 통해 유효성 체크

# 모든자리에 1씩 증감해서 곱하고 9넘어가면 2부터 다시 루프 여기에서 sum 값이 11나누었을 때 나머지 값에서 11을 뺀 값이 마지막 번호
#이렇게 무식허게 해야돼?????? for로 어떻게 허지?? 
RRN="990112-1234567"
sum=int(RRN[0])*2+int(RRN[1])*3+int(RRN[2])*4+int(RRN[3])*5+int(RRN[4])*6+int(RRN[5])*7+int(RRN[7])*8+int(RRN[8])*9+int(RRN[9])*2+int(RRN[10])*3+int(RRN[11])*4+int(RRN[12])*5
sum%=11
final_num=11-sum

if str(final_num)==RRN[-1]:
    print("유효")
else:
    print("유효 X")


#======5/25 수업=====
#for는 범위가 명확하다
# 컨티뉴는 반복문에서만 사용가능하고
#pass는 모든 구문에서 사용가능하다(거의 동일하게 사용된데)

#====연습문제3 5/25======
# for문과 range() 활용하여 1~10까지 곱한 변수를 sum에 저장하시오.
sum=1
for i in range(1,11):
    sum*=i

print(f"1부터 10까지 곱한 값 {sum}")

#seq와 비슷해~~~ 인터벌(간격) 지금은 증감간격, 감속감격도 가능함
for i in range(11,1,-2):
    print(i, end=" ")


#====연습문제4 5/25======
#50점 이상 획득자에서 1번째 수험생은 합격, 50점 미만자는 미출력
#1. for, if, else 활용
#2. for, if만 활용
score=[99,80,60,40,67]
num=0
# 1.
# for i in score:
    # num+=1
    # if i>=50:
        # print(f"{num}번째 {i}점 합격")
    # else:
        # 아무것도출력하지 않아서 
        # continue

# 2. 자주 사용하는 패턴과 비슷함 (들여쓰기가 이상해!!! 실행확인)
for i in range(len(score)):
    if score[i]>=50:
      print(f"{i+1}번째 합격")
      
      
      
#====연습문제5 5/25  이중 for 드디어 올것이 왔다 이렇게 끝났어? ㄷㄷㄷㄷㄷ 무섭다 ======
#2-9 구구단 출력 와~~~~ 파이썬 넘나 쉽게 만들수 있구나 범위 지정이랑 문자지정이 너무 쉬워~~
for i in range(2,10):
    print("\n")
    for j in range(1,10):
        print(f"{i}*{j}={i*j}", end="\t")
        
        
        
#====와일문 5/25======
#와일문의 안전장치 break 여기서 브레이크를 넣는다면?! 실행이 되다가 멈춘다~~~
#지금 와일문의 예시는 for문과 같이 범위가 있음 →블리언(T,F)으로 쓰고 break로 한다 
print("\n")
throws=0
while throws<10:
    throws+=1
    print(f"공 던지기 {throws}회 하였습니다")
    if throws==10:
        print("오늘의 연습을 마쳤습니다.")


#좀 더 와일문 형식에 맞음 
throws1=0
while True:
    throws1+=1
    print(f"배트연습 {throws1}회 하였습니다")
    if throws1==5:
        print("오늘의 연습을 마쳤습니다.")
        break