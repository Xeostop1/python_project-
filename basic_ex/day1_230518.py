# ab="안녕"
# ,로 연결하면 띄어쓰기로 연결되고, +는 띄어쓰기 없이 연결됨 
# ''' ''' 여러줄 주석처리
#javascript처럼 ", '둘다 아무거나 사용해도 무방함
# 아 파이썬도 와일문 써야 되네 ㅠㅠ
'''print(ab)
print(ab,"하세요")
print(ab+"하세요")'''
# print(ab)

greeting="안녕하세요"
print(greeting)

# a=10
# print(a)

name="둘리"
age=10
age_1="10"
print(type(age))
print(type(str(age)))
print(type(repr(age)))
location="쌍문동"


def introduce(name, age, location):
    print("제 이름은 "+name+"입니다. 저는 "+str(age)+"살이고", location+"에 삽니다")

introduce(name, age, location)


print("제이름은 "+name+"입니다. 저는 "+str(age)+"살이고"+location+"에 삽니다")
print("제이름은 "+name+"입니다. 저는 "+age_1+"살이고"+location+"에 삽니다")