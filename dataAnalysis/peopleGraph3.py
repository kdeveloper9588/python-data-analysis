import csv
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
filename = '/content/drive/MyDrive/Colab Notebooks/age.csv'
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)
head = next(data)
rs = []
loc_name = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요. :')
for row in data:
    if loc_name in row[0]:
        for i in row[3:]:
            rs.append(int(i.replace(',', '')))
f.close()
print(rs)

plt.rc('font', family="NanumBarunGothic")
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')
plt.barh(range(101), rs)
plt.show()
