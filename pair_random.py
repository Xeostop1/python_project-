from random import *
#어떻게 알았지??ㅋㅋㅋ 

websites=["마켓컬리", "야놀자", "아고다","아마존","웨이브","펫프렌즈","인터파크티켓","마이리얼트립","네이버항공권"]

stus= ['강성진', '권재원', '김은아', '김은진', '김현하', '박수현', '서지연', '서하나', '신화영',
          '이가빈', '민정식', '이현희', '이혜리', '이혜원', '임서희', '조유진', '주서현', '홍선희']



#====리스트를 파라미터로 하고, 랜덤 리스트를 리턴하는 함수
#근데 왜 나 안되지??? 
# def shuffle_list(list):
    # random_nums=[]
    # randomized_list=[]
    # while True:
        # random_num=randrange(len(list))
        # 파이썬은 not in 사용  / 자바는 이중 포문 돌려서 i=j 같이 비교함! 
        # 배열 안에는 in 으로 살펴봐도 되네 
        # if random_num not in random_nums:
            # random_nums.append(random_num)
        # if len(random_nums)==len(list):
            # break
        # for i in random_nums:
            # randomized_list.append(list[i])
        # return randomized_list    


# print(shuffle_list(websites))

#파이썬은 그게 편하구나 들여쓰기 하고 앞에 선언만 해주면 된다! 
def pair_list(list):
    paired_list=[]
    #어차피 위에 랜덤을 돌려줘서 여기서는 굳이 랜덤을 안해도 로상관
    #여기서 range를 쓰는구나~ 천잰데??? (range()의 인터벌을 통해 2개씩 묶어서 리스트에 넣어버리기 *0*,1→ 2인터벌→*2*.3)
    for i in range(0, len(list),2):
        paired_list.append([list[i],list[i+1]])
    return paired_list


    
res2=pair_list(stus)
# print(res2)


def set_list(list,title_list):
    seted_list=[]
    for i in range(len(list)):
        seted_list.append([list[i],title_list[i]])
    return seted_list



res3=set_list(res2, websites)
print(res3)


# while True:
    # random_num=randrange(len(websites))
    # 파이썬은 not in 사용  / 자바는 이중 포문 돌려서 i=j 같이 비교함! 
    # 배열 안에는 in 으로 살펴봐도 되네 
    # if random_num not in random_nums:
        # random_nums.append(random_num)
    # if len(random_nums)==len(websites):
        # for i in random_nums:
            # random_webs.append(websites[i])
        # break

        
