#=====함수======
from random import *
#randrange(5) : 0부터 4까지 랜덤 
# import random
# 이렇게 쓸 경우 random. 하고 사용




def select_title(people, title_num):
    shuffle(people)
    pair=[]
    for i in range(len(title_num)):
        title = []
        # pop(x)는 리스트의 x번째 요소를 리턴하고 그 요소는 삭제.*2하는 이유 두명 추출할려고
        title.append(people.pop())
        title.append(people.pop())
        pair.append(title)
        print(f"{title_num[i]}:  {title[0]} / {title[1]}")
    return pair

websites=["마켓컬리", "야놀자", "아고다","아마존","웨이브","펫프렌즈","인터파크티켓","마이리얼트립","네이버항공권"]

stu = ['강성진', '권재원', '김은아', '김은진', '김현하', '박수현', '서지연', '서하나', '신화영',
          '이가빈', '민정식', '이현희', '이혜리', '이혜원', '임서희', '조유진', '주서현', '홍선희']

pair_title = select_title(stu, websites)
# print(pair_title)


# random_num=randrange(len(websites))

random_nums=[]
while True:
    random_num=randrange(len(websites))    
    #파이썬은 not in 사용 자바 같은 경우는 / 이중 포문 돌려서 i=j 같이 비교함! 
    #배열 안에는 in 으로 살펴봐도 되네 
    if random_num not in random_nums:
        random_nums.append(random_num)
    if len(random_nums)==len(websites):
        break





# for i in range(len(websites)):
    # random_num=randrange(len(websites))
    # if random_nums==random_num:
        # continue
    # random_nums.append(random_num)




def random_num(list_len):
    res=randrange(len(list_len)+1)
    print(res)
    
random_num(stu)



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

#====연습문제6 5/25======
# 숫자를 입력 받아 해당 숫자가 정수, 양의 정수인지 확인 하고 
# 양의 정수 일 경우 홀짝 판별하고 홀짝을 프린트하는 출력하는 함수 
# 양의 정수가 아닐 경우 양의 정수만 입력해 주세요
# 정수가 아닌 숫자를 입력 받았을 경우 정수가 아닙니다. 도 출력 
#힌트: 정수 판별을 위해 함수 내 if문 type(파라미터)==int 조건식을 넣어 활용

print(" ")

def odd_even(num):
    if type(num)!=int:
        print(f"{num}은 정수가 아닙니다 정수를 입력해 주세요")
    elif num>0:
        if num%2==0:
            print(f"{num}은 짝수 입니다")
        else:   
            print(f"{num}은 홀수 입니다")
    if num<=0:
        print(f"{num}은 양의 숫자가 아닙니다 양의 정수만 입력")
    
    
    
#====선생님 버전=====
def screen_num(num):
    if type(num) ==int:
        if num>0:
            if num%2==0:
                print("짝")
            else:
                print("홀")
        else:
            print("양의 정수만 입력")
    else: 
        print(f"{num}은 정수가 아닙니다")

odd_even(0)
screen_num(0)
        
#====연습문제1 5/26======
#두개의 값을 파라미터로 받아 더해서 결과값을 돌려주는 함수 작성
def return_ex(a,b):
    return a+b
    
res=return_ex("hi","nana")
print(res)

#====연습문제2 5/26======
# 문자를 입력 받아 "OO님 안녕하세요" 문장을 반화하는 함수를 작성
# 프린트없이 포맷팅만 단일 사용이 가능하네 
def say_hi(name):
    return f"{name}님 안녕하세요"    
print(say_hi("cola"))


#====연습문제3 5/26======
# 세개의 파라미터 받는 함수, 2개는 기본값으로 5000,10 할당 
# 함수 호출 시 요청하신 과일은 OO입니다. 가격은 OOO이고 최소 구매수량은 OO입니다 출력 
# 초기값은 1순위가 될 수 없음
def item_info(item,price=5000,qty=10):
    return f"요청하신 과일은 {item}입니다. \n가격은 {price}원이고, 최소수량은 {qty}개입니다"
    
    
print(item_info("사과"))
print(item_info("포도",3000, 5))


#====연습문제3 5/26======
# 임의의 숫자 여러개를 인자로 받아 전달된 인자의 합을 구한 후 반환 하는 함수

def add_all(*num):
    sum=0
    for i in num:
    #i 값이 항상 T로 평가됨 
    #안되는 이유 i가 정수이면서 부동 소수점이 될 수 없기 때문에 
       if type(i)==int or type(i)==float:
        print(f"입력하신 숫자는 {i}")
        #pass 적어줘서 문제없으면 다음으로 패스 
        pass
       else:
        print(f"{i} 숫자가 아님")
        #숫자를 만나면 리턴있어서 더이상 실행 안됨
        return
    
print(add_all(1,2,"3",3.6))

#====연습문제18 5/26======
# 첫번째 파라미터부터 두번째 파라미터 미만까지 임의이 수를 반환하는
# randrange()