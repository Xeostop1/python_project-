#list ≒ 배열
#리스트는 복합형 (리스트 +리스트도 가능함)


a=["hello", "I", "have", [1,"apple"]]
print(a[0])
print(a[3])
print(a[-1])
#2번 인덱싱 가능! 
print(a[-1][1])

#=====리스트 연산====
#리스트+ 하면 그냥 통합됨 
a=[1,2,3]
b=[4,5,6]
print(a+b)

#===리스트 추가====
a=[1,2,3,4,5]
a.append(6)
print(a)
a.append([7,8])
print(a)
a.insert(0,300)
#인설트는 인덱스로 넣을 수 있는데 
#어팬드는 인덱스로 넣을 수 업음!!! 
print(a)
#그래서 오류!! 
a.append(9)
print(a)


#===리스트 삭제====
del a[0]
print(a)

del a[3]
print(a)

#===리스트 수정====
a[0]=0
print(a)
print("**")
for i in a:
    print(i, end="")

print("***")
a=[1,2,3,[4,5,6,7,8]]
print(len(a[3]))

#=====sort====
a=[1,2,3,0]
a.sort()
print(a)
a.reverse()
print(a)

#====튜플=====
#()로 사용 수정,삭제,추가 불가능 
#FINAL 같은 건가봐 묶어나 버렸네(불변 데이터) 
# 튜플은 일반적으로 목록보다 메모리 효율적이고 처리 속도가 빠릅니다. 
#변경되지 않는 값 모음이 있는 경우 목록 대신 튜플을 사용하면 성능이 약간 향상될 수 있습니다.

t=1,2,3
print(t)
t1=(1,)
print(t1)
