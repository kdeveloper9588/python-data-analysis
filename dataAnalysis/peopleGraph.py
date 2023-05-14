# 읽어온 데이터를 리스트에 저장
import csv
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

filename = '/content/drive/MyDrive/Colab Notebooks/age.csv'
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)
head = next(data)
rs = []
for row in data:
    if '장전제1동' in row[0]:
        for i in row[3:]:
            rs.append(int(i.replace(',', '')))
f.close()
plt.style.use('ggplot')
plt.plot(rs)
plt.show()
