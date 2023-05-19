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