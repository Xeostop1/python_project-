#=====함수======
import random

def select_title(people, title_num):
    random.shuffle(people)
    pair=[]
    for i in range(title_num):
        title = []
        # pop(x)는 리스트의 x번째 요소를 리턴하고 그 요소는 삭제.*2하는 이유 두명 추출할려고
        title.append(people.pop())
        title.append(people.pop())
        pair.append(title)
        print(f"Title {i+1}: {title[0]} / {title[1]}")
    return pair

people = ['강성진', '권재원', '김은아', '김은진', '김현하', '박수현', '서지연', '서하나', '이가빈',
          'Person10', 'Person11', 'Person12', '이현희', 'Person14', '신화영', '이아름', 'Person17', 'Person18']

pair_title = select_title(people, 9)
# print(pair_title)



#====함수의 초기값 5/25======
#파라미터에 초기값 바로 넣고 설정가능, 파라미터로 따로 넣어주지 않으면 초기값을 이용
print("\n")
def purchase(i, price=5000):
    print(f"{i}는 {price}입니다")

purchase("사과",3000)
purchase("포도")

#=====매개변수를 지정하여 전달=====
#아규먼트에 변수로 바로 넣고 사용가능

def divide(a,b):
    print(a/b)


divide(a=10, b=5)
divide(b=10, a=5)

#===미지정 파라미터: *사용(가변성파라미터)=====
#======*을 입력하면 정해지지 않은 여러개의 전달 대신 파라미터를 ***튜플***로 저장

def changealbe(*args):
    print(type(args))
    for i in args:
        print(i)

changealbe(1,2)

def changealbe2(a,*args):
    print(type(args))
    print(type(a))
    print(a, args)

changealbe2("num",1,2,3,4)


#====연습문제1 5/25======
# 1-10까지 파라미터로 넣어 1-10까지 출력하는 함수 
# 파라미터에 가변성파라미터 사용 for을 넣어 활용
def sum_all(*num):
    for i in num:
        print(i,end=" ")

sum_all(1,2,3,4,5,6,7,8,9,10)


#====연습문제2 5/25======
# 합을 구하는 함수를 저장 
print("\n")

def sum_all2(*num):
#굳이 리스트로 변경안해도 되네, 사칙연산은 가능한가봐 직접 수정말고, 변수로 넣어서 보여 줄 수 있네
    sum=0
    for i in num: 
        sum+=i        
    return sum
    
print(sum_all2(1,2,3,4,5,6,7,8,9,10))


#====연습문제3 5/25======
# "mul" 또는 "add"로 전달하고 1~10까지 파라미터를 넣어 호출, 
# 1 파라미터가 mul일 경우 1~10까지 곱하고, 1파라미터가 add라면 1~10까지 합하는 리턴함수
#**** 들여쓰기 조심할것!!!!!******

def sum_mul(keyword,*item):
    if keyword=="mul":
        mul=1
        for i in item:
            mul*=i
        # print(f"모두 곱한 값은 {mul}")
        return mul
    elif keyword=="add":
        sum=0
        for i in item:
            sum+=i
        # print(f"모두 더한 값은 {sum}")
        return sum
    else:
        print("keyword를 mul 또는 sum으로 적어주세요")

r1=sum_mul("add",1,2,3,4,5,6,7,8,9,10)
r2=sum_mul("mul",1,2,3,4,5,6,7,8,9,10)
r3=sum_mul("mul2",1,2,3,4,5,6,7,8,9,10)

print(r1)
print(r2)
print(r3)

#마지막 엘스 프린트문이 찍히고(함수안에 있는 프린트 명령문이라서 )
#다음부터 나옴) 


#====연습문제4 5/25======
# 2개의 파라미터 함수 매개변수명 price item 프라이스는 초깃값 3000설정
# 출력은 포맷팅 사용 "OOO은 OOO원 입니다"
# 초기값은 뒤에 넣어줘야 하나봐 앞에 넣으니까 않돼 why???
def price_info(item,price=3000):
    print(f"{item}는/은 {price}입니다")
    
price_info("사탕")
price_info("프링글스",1500)

#====연습문제5 5/25======
# 정하지 않은 여러개의 숫자를 파라미터로 하여 입력된 숫자의 평균을 구하고 
# "평균점수는 OO 입니다"를 출력하는 함수 포맷팅 이용

def score_avg(*score):
    sum=0
    avg=0
    for i in score:
        sum+=i
    avg=int(sum/len(score)) 
    print(f"평균점수는 {avg}입니다 ")
    return avg

score_avg(10,10,10)


# 중복안되는 것을 찾아서 공항고유 코드를 찾아야 한다 