import csv
import matplotlib.pyplot as plt
from google.colab import drive
filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
next(data)
month = [[], [], [], [], [], [], [], [],
         [], [], [], []]  # 최고 기온 데이터를 저장할 리스트 생성
for row in data:
    if row[2] != '':  # 데이터 값이 있을 경우에 만
        month[int(row[0].split('-')[1])-1].append(float(row[2]))

f.close()
plt.title('1월 8월 최대기온')
plt.boxplot(month)
plt.show()
