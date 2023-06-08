import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

import matplotlib
from matplotlib import font_manager, rc
import platform

#=====한글세팅=====
if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:    
# Mac 인 경우
    rc('font', family='AppleGothic')
    
matplotlib.rcParams['axes.unicode_minus'] = False  

import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:    
# Mac 인 경우
    rc('font', family='AppleGothic')
    
matplotlib.rcParams['axes.unicode_minus'] = False  
#===========================================

#====중복단어제거=============
import pandas as pd
import matplotlib.pyplot as plt

def remove_duplicates(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words


# 데이터
data = ['전라', '문화', '문화', '해양', '문화', '해양', '농수산물', '전라']

# 각 카테고리의 빈도수 계산
category_counts = pd.Series(data).value_counts()

# 정렬
category_counts = category_counts.sort_values(ascending=False)

print(category_counts)

title = remove_duplicates(data)
print(title)

# 그래프 그리기
sorted_title = category_counts.index.tolist()  # 정렬된 카테고리 리스트
sorted_counts = category_counts.tolist()  # 정렬된 빈도수 리스트

plt.bar(sorted_title, sorted_counts)
plt.xticks(rotation=0)

plt.show()


# 특정 카테고리 차단
# blocked_categories = ['문화', '해양']
# category_counts_blocked = category_counts.drop(blocked_categories)

# # 막대 그래프 생성
# plt.bar(category_counts_blocked.index, category_counts_blocked.values)

# # 제목과 축 레이블 설정
# plt.title('카테고리별 빈도수 (차단됨)')
# plt.xlabel('카테고리')
# plt.ylabel('빈도수')

# # 그래프 표시
# plt.show()
