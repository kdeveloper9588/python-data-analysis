import csv
from google.colab import drive
drive.mount('/content/drive')

filename = '/content/drive/MyDrive/Colab Notebooks/age.csv'
f = open(filename, 'r', encoding='cp949')
data = csv.reader(f)
head = next(data)
for row in data:
    print(row)
f.close()
