#1. 아래의 코드중에 에러를 발생시키는 코드를 찾아 주석처리 
# b 변수를 선언하지 않아서 name 'b' is not defined 에러 발생 
a="10"
print("a의값은 "+a+"입니다");
# print("b의 값은"+b+"입니다");

#=============================================
# 2.결과물이 나오지 않도록 최소한의 주석처리하기 
# 변수선언을 주석처리 하여 결과물 미 산출 
a="20"
b="20"
print("a의값은 "+a+"입니다");
print("b의값은 "+b+"입니다");

#=============================================
# 3. 에러가 발생하는 코드 수정
#1번에러: 들여쓰기 
#2번에러: 숫자열이나 문자열로 변환 
# 해결방법: 1 c를 문자열로 변환, str()사용

c=10
if(c):
    print("c의값은 "+str(c)+"입니다");     

#=============================================
#4. 에러코드 수정
print("안녕하세요. 반갑습니다")
# print("안녕하세요. 반갑습니다')

#=============================================
# 5. name, age, loction 변수를 사용하여 아래 문장을 출력 age는 숫자형으로 설정
# 제 이름은 김철수입니다. 제 나이는 10살입니다. 저는 서울에 살고 있습니다.
# 숫자형을 문자열로 변환 (3번문제의 응용문제) 
# type()으로 확인
name="김철수"
age=10
location="서울"
print("제 이름은 "+name+"입니다. 제 나이는 "+str(10)+"살입니다. 저는"+location+"에 살고 있습니다")
#========================================================================================


i=10
j=5.5
x=12
print(i)
print(type(i))
print(j)
print(type(j))
print("check",type(int(i+j)))
print(type(i*j))
#========================================================================================
#제곱 연산자
#****중요*****
kai=2
x=3
print(kai**x)

#========================================================================================
#나머지 연산자(홀짝 판별, 자리수 이동 등에 사용)
a=8%3
b=2%5
c=4%1
print(a,"나머지")
print(b,"나머지")
print(c,"나머지")
#========================================================================================
#몫 연산자(홀짝 판별, 자리수 이동 등에 사용)
a=7/5
b=7//5
print(a,"몫")#float의 형태로 반환 
print(b,"몫") #//는 인트로 반환

#========================================================================================
# 숫자 관련 함수
a=10
b=20
c=20.3
d=20.5
e=-9
#절대값
print("절대값",abs(e))
#제곱
print("제곱",pow(a,b))
#최대값
print("최대값",max(a,b))
#최소값
print("최소값",min(a,b))
#반올림
print("반올림",round(c))
print(round(d))
#정수값
print("인트형 반환",int(c))
#========================================================================================
# Math 사용
from math import *
print(floor(c))

#=============================================
# 연습문제 1
# 1. 타입 출력 (a,b)
# 2. a 정수, b 실수 변환출력
# 3. a 반올림

a=3.14
b=4

print("a",type(a))
print("b",type(b))
print("a 정수",int(a))
print("b",float(b))
print("a 반올림",floor(a))
#=============================================
# b를 a로 나눈 몫 and 나머지
a=4
b=5
print(b//a)
print(b%a)

#=============================================
# a의 절대값, b를 변수로 a 제곱, abc 중에  max, min
a=-4
b=5
c=2
print(abs(a))
#둘다 같은 값
print("제곱값",pow(b,a))#헷갈린다 뒤가 지수, 앞에 제곱할 수 
print("제곱값",b**a)#헷갈린다
print("max",max(a,b,c))
print("min",min(a,b,c))
#=============================================
# 올림과 내림
a=1.2
print("올림",ceil(a)) #씰이고 씰링과 관련이 있나봐(: 의 최대 한계[상한] 뜻이 있데)
print("내림",floor(a))
#=============================================
# 랜덤에서 정수 10개 출력
from random import *
a=(random()*10)+1
#이렇게 해도 되고,randrange()도 있데 #왜 안되지???? 확인하기 →단독만 사용해야 되나봐 random.이 아니고 
b=randrange(1, 10)
print(int(a))
print(int(b))
#=============================================
# 랜덤으로 1~75 사이 정수 10개 출력 
'''a= (random()*75)+1
print("랜덤값",int(a))
arr_test=[10]
arr_test.append(int(a))
for i in arr_test:
    print(i)'''
    
a=5
b=0
if a:
    print("a True")

if b:
    print("b F")

 #숫자자료 비교 
if(5>3):
    print("5는 3보다 큽니다")
    
#문자열 비교가 안되나?? 유니코드로 못하나? → 유니코드로는 가능함    
if("a">"A"):
    print("a는 A보다 큽니다")
    
#bool*()
print("불리언 검사",bool([1,2]))
a=" "
print(bool(a))
    