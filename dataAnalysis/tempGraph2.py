# 매년 스승의 날인 5월 15일의 최고 기온 데이터에 대한 그래프 그리기
import csv
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')

f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
next(data)
rs = []  # 최고 기온 데이터를 저장할 리스트 생성
for row in data:
    if row[2] != '':  # 데이터 값이 있을 경우에 만
        if row[0].split('-')[1] == '05' and row[0].split('-')[2] == '15':  # <-여기 추가
            # if row[0].split('-')[2] == '15':위에랑 같음
            rs.append(float(row[2]))
f.close()
plt.plot(rs, 'r')
plt.show()
