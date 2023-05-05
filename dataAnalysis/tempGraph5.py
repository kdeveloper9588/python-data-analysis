# split()함수를 사용해 1년 중 여름의 정점인 8월 최고 기온 데이터만을 추출해서 그래프로 그리기
import csv
import matplotlib.pyplot as plt
from google.colab import drive
filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')

filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
next(data)
rs = []  # 최고 기온 데이터를 저장할 리스트 생성
rs2 = []
for row in data:
    if row[2] != '':  # 데이터 값이 있을 경우에 만
        if row[0].split('-')[1] == '08':  # <-여기 추가
            rs.append(float(row[2]))
        if row[0].split('-')[1] == '01':
            rs2.append(float(row[2]))
f.close()
plt.title('1월 8월 최대기온')
plt.hist(rs, bins=100, color='r', label='8월 기온')
plt.hist(rs2, bins=100, color='b', label='1월 기온')
plt.legend()
plt.show()
