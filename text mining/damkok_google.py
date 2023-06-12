import os
import csv
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 파일이름
csv_file = "google_damkok.csv"

#scv 읽고 추출
data = ""
with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        data += " ".join(row) + " "

# 단어를 추출하고 각 단어의 빈도계산(숫자제외)
words = re.findall(r"[가-힣]+", data)
word_counts = Counter(words)

# 높은 빈도 10 추출
most_common_words = word_counts.most_common(10)

# 단어와 빈도를 분리
words, frequencies = zip(*most_common_words)

# 한글 폰트 경로를 설정. 필요한 폰트 파일(.ttf)을 별도로 다운로드하여 경로를 지정
font_path = "KoPubWorld Batang Medium.ttf"  

# WordCloud 객체를 생성하고 단어 빈도로부터 워드 클라우드를 생성
wordcloud = WordCloud(width=800, height=400, background_color="white",
                      font_path=font_path).generate_from_frequencies(word_counts)

# 워드 클라우드를 시각화
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("가장 빈도가 높은 단어")
plt.show()
