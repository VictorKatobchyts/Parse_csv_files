import csv
import re
from itertools import groupby
keys = []
with open('C:\\Users\\Sailwork\\Desktop\\parse\\Parse_csv_files\\TestData.csv') as csvfile:#C:\Users\Sailwork\Desktop\parse\Parse_csv_files\TestData.csv
    a=0
    csv_read = csv.reader(csvfile, delimiter=';')
    for row in csv_read:
        a+=1
        if  (a>1 & a <101):
            new_string = re.sub("[\|[\]]",'', row[4])
            new_string = new_string.replace("'","!")#заменяем все апострофы на восклицательные знаки, чтобы не багалось
            new_string = new_string.split(',')
            del new_string[0:2]
            keys.append(new_string)
            new_keys = [el for el, _ in groupby(keys)]
            print(new_keys)   