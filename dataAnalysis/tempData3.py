# 데이터를 리스트에 저장
import csv  # csv 불러오기
from google.colab import drive
filename = ('/content/drive/MyDrive/Colab Notebooks/busan.csv')  # 코랩 드라이버 연결

f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
next(data)
rs = []  # 최고 기온 데이터를 저장할 리스트 생성
for row in data:
    if row[2] != '':
        rs.append(float(row[2]))
f.close()
print(rs)
