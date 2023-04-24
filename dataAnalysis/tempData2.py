import csv
import csv  # csv 불러오기
from google.colab import drive

# 부산의 기온이 가장 높았던 날의 날씨와 기온 구하기
filename = '/content/drive/MyDrive/Colab Notebooks/busan.csv'

f = open(filename, 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')  # <=생략가능
header = next(data)
max_temp = -999
max_date = ''
for row in data:
    if row[2] == '':
        row[2] == -999
    row[2] = float(row[2])
    if max_temp < row[2]:
        max_date = row[0]
        max_temp = row[2]
f.close()
print(max_date, max_temp)
