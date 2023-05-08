import csv
from google.colab import drive
import matplotlib.pyplot as plt
filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
next(data)
day = []
for i in range(31):
    day.append([])

for row in data:
    if row[2] != '':  # 데이터 값이 있을 경우에 만
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[2]))
f.close()
plt.style.use('ggplot')  # 그래프 스타일 지정 : 회색 격자 무늬 스타일
plt.figure(figsize=(10, 5), dpi=100)  # 그래프 키기 수정: 가로 10 세로 5  dpi는 해상도
plt.boxplot(day, showfliers=False)  # 우웃라이어 값 생략
plt.show()
