import csv

words = {'detox drinks','MOBILE'}
with open('out.csv', 'w') as out:
    for line in csv.reader(open('C:\Users\Sailwork\Desktop\Парсинг файлов\TestData.csv')):
        if words & set(line):
            out.write(','.join(line))