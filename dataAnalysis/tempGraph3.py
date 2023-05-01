# 2005년 이후의 데이터만 받아서 5월 15일을 기준으로 최고/최저 기온에 대한 그래프 그리기
import csv
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')

f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
next(data)
high = []  # 최고 기온 데이터를 저장할 리스트 생성
low = []
for row in data:
    if row[2] != '':  # 데이터 값이 있을 경우에 만
        if 2005 <= int(row[0].split('-')[0]):
            if row[0].split('-')[1] == '05' and row[0].split('-')[2] == '15':  # <-여기 추가
                # if row[0].split('-')[2] == '15':위에랑 같음
                high.append(float(row[2]))
                low.append(float(row[4]))
f.close()
plt.title('스승의 날의 기온 변화 그래프')
plt.plot(high, 'r', ls='-', label='최고기온')
plt.plot(low, 'g', ls='-', label='최저기온')
plt.legend()
plt.show()
