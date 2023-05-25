greeting="Hello, I\'m Korean"
print(greeting)
say="He said, \"I will be back\""
print(say)

greeting="Hello \n I'm Korean"
print(greeting)
g="hello"
g2="Nice to meet you"
g3=g+g2
print(g3)
print(g*3)


word="apple"
print(len(word))
print(word[2])

#문자열에서는 레터라고 부른데(레터가 아니고 )
# 역순접근은 이미지, 
print(g[-1])
print(g[-5])
#****0포함 2미포함***********
print(g[0:2])
#공란이라면 0부터 시작점부터 출발 
print(g[:2])
#인덱스 1부터 시작점
print(g[1:],"확인") 
print(g[:])
print(g[:-3])
#뒤에서부터 접근 -1-2-3

#포맷팅 자체가 문자열 형식지정이 맞네 
# 형식화라는 말이 너무 어려워 
#=======문자열 포맷팅(총 3가지 방식이 존재)======
#문자열에 변수를 직접 넣기 근데 왜 %을 쓸까??? 
print("It is a %s day" %"happy")
print("it is %d in the morning" %6)
print("It is %d in the %s" %(8, "day"))

num=2
siblings="brothers"
family="I have %d %s "%(num, siblings)
print(family)

#=====format 사용(제일 많이 사용)====
print("It is {} day".format("happy"))
print("It is {} in the morning ".format(9))
print("It is {} in the {}".format(6, "night"))
# b=a.format()

#제일 많이 사용하는 형태 
weather="sad"
print(f"It is a {weather} day")


#아 클래스를 안나가는구나

capital="ABCD".lower()
print(capital)
capital="ABCD".isupper()
capital="ABCD".replace("C","X")
print(capital)

#====18~19page 연습문제====
a="hello"
b="World!"
print(a,b)
print(a*3)
print((a+"\n")*3)
print(len(a+b))
c="He said, \"I'm fine\""
print(c)

RRN="901225-1234567"
a=RRN[:6]
print(a)
b=RRN[7:]
# b=RRN[-7:]
#나는 괜히 뒤에서 부터 했네 ㅋㅋ 
print(b)
print(a+"-"+b)
print("{}-{}".format(a,b))
print("%s-%s"%(a,b))

#====20 연습문제====
print("지금은 {} {} 입니다".format("오전",7))
print("지금은 {} {} 입니다".format("오후",5))


