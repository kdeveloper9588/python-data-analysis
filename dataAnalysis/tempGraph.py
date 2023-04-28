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
    if row[2] != '':
        rs.append(float(row[2]))
f.close()
plt.plot(rs, 'r')  # 최고기온 그래프를 빨간색으로
plt.show()
