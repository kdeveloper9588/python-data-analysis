import csv  # csv 불러오기
from google.colab import drive
drive.mount('/content/drive')  # 구글 코랩 드라이브 연결

filename = '/content/drive/MyDrive/Colab Notebooks/busan.csv'  # 파일 경로

f = open(filename, 'r', encoding='cp949')
data = csv.reader(f, delimiter=',')  # <=생략가능
for row in data:
    print(row)
f.close()
