def createLine(str):
    print(str)

a=True
b=False
print(type(a))
a=5
b=5
print("1",a==b)
print("2",5==5)
print("3",5>3)
print(5<3,"4")
# 최대 가져올 페이지 선언 후 if에서 조건 검사
'''max_page=10
currnt_page=find(페이지렝스)
if(currnt_page==max_page+1):
    stop()'''
    
#============연습문제 6 5/19==============================
# a에 1000 할당 a가 30%하락 했다면 계산결과를 a에 저장 정수형태로 출력 
a=1000
a*=0.7
print("a가 30% 하락한 결과값 ",int(a))


def persent(num):
    res=num-(num*0.3)
    return print("a가 30% 하락한 값은",int(num))

persent(a)

#============연습문제7 5/19==============================
# 사과 3000/50 오렌지 2000 /100 모든 과일을 파매할 경우 얼마 매출 발생 프린트 할때 원으로 표시
apple=3000
orange=2000
a_num=50
o_num=50
sum_res=(apple*a_num)+(orange*o_num)
print("총판매 금액은 "+str(sum_res)+"원 입니다")


# def sale(num1,num2):
    # sum_res=(global apple*num1)+(global orange*num2)    
    # print("모든 판매 금액은 "+str(sum_res)+"원 입니다")

# sale(50,100)
#============연습문제8 5/19==============================
# 판매가격이 상승해서 10% 15%일때 매출량 계산 
a_in=1.1
o_in=1.15

sum_res1=(apple*a_num*a_in)+(orange*o_num*o_in)
print(sum_res1)

#비교연산자
#==양쪽 값 동일
#!= 양쪽 값이 동일하지 않음
# >= 왼쪽이 오른쪽 보다 크거나 같다 
# <= 왼쪽이 오른쪽 보다 작거나 같다 
a=1
b=2
# 조건문이나 반복문에서 이런 논리값을 사용
# 계속 ,로 연결되네
print(a==b)
print(a!=b)
print(a>b)
print(a<b)

#========할당연산자=============
# /= 왼쪽에 오른쪽 값을 나눈 결과를 왼쪽 변수에 할당 
# %= 왼쪽에 오른쪽 값을 나눈 나머지를 왼쪽 변수에 할당 
# //= 왼쪽에 오른쪽 값을 나눈 몫만!!를 왼쪽 변수에 할당 
# **= 왼쪽에 오른쪽 값을 제곱한 결과를 왼쪽 변수에 할당 
#and 파이썬에서는 && 대신사용 → & 이거 1개만 쓴데!!아이고 헷갈려
#or 파이썬에서는 || 대신사용 → | 이거 1개만 사용!! 비트연산자랑 헷갈리는 구만 
#not 파이썬에서는 != 대신사용

c=13
d=True
print(a<b and a>c, "and 연산자 ")
print(a<b or a>c, "or 연산자 ")
print(not d)
#그러면 not 이랑 !=이랑 같이 쓰이나?? 
print(d!=d)

#===========연습문제 5/22========
print(3!=3,"F")
print((2>=1)&(3<=3),"T")
print((5<=10)&(3<=3),"T")
print((4<10)|(7>8),"T")
print((4>10)|(7>8),"F")
print((4<10)|(7<8),"T")



#===========연습문제3 5/22========
#일 때 코드를 작성
a=2
b=3 
# 1. ab을 나눈 나머지
print(a%b, "1번")
# 2. a를 b로 제곱한
print(a**b, "2번")
# 3. a에 a와  b를 더한 값
a+=b
print(a,"3번")
# 4. a에 a와  b를 곱한 값
a*=b
print(a,"4번")
# 5. a를 b로 나눈 몫
print(a//b, "5번")
# 6. a에  a를 b로 나눈 몫 대입
a/=b
print(a,"6번")

#===========연습문제9 5/22========
# 타입을 출력하는 코드 작성
createLine("#===========연습문제9 5/22========")
a=10
b="안녕하세요"
c=True
print(type(a))
print(type(b))
print(type(c))

createLine("#===========연습문제10 5/22========")
# 실수는 정수 정수는 실수로 
b=2.5
print(float(a))
print(int(b))
# 변수 자체가 변한게 아니니까~~~~

createLine("#===========연습문제11 5/22========")
# 1~3000 까지의 숫자 중 임의의 숫자 하나를 변수 a에 할당한다면 
#a가 홀수일 경우 "a는 홀수"을 출력하는 if문을 작성하시오 

from random import *
num=randrange(1,3001)
#num=randint(1, 3000)
# num=int((random()*3000)+1)
if(num%2==1):
    print(num,"홀수입니다")
else:
    print(num,"짝수입니다")
    
"""
나쁘지 않은데?? 
선생님 답은 위에서 변수에 2을 나눈 몫을 True 상태로 주고 
if result:
    print()로 돌아가게 세팅 
나는 if에서 세팅했고 선생님은 변수에 먼저 플래그 걸어준거임 """
