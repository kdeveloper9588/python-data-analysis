import csv
from google.colab import drive
drive.mount('/content/drive')

filename = '/content/drive/MyDrive/Colab Notebooks/age.csv'
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)
head = next(data)
for row in data:
    if '우제1동' in row[0]:
        for i in row[3:]:
            print(i, end=' ')
f.close()
