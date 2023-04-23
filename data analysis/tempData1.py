import csv
from google.colab import drive
drive.mount('/content/drive')  # 코랩 드라이브 연결

filename = '/content/drive/MyDrive/Colab Notebooks/busan.csv'

f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)  # <=생략가능
for row in data:
    print(row[2])  # 최고기온 출력
f.close()
