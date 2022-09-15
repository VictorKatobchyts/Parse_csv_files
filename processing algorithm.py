import csv
import re

with open('C:\\Users\\Sailwork\\Desktop\\parse\\Parse_csv_files\\TestData.csv') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=';')
    a=0
    for row in csv_read:
        a +=1
        if (a == 2):
            print(row[4])
            new_string = re.sub("[\|[\]]",'', row[4])
            print(new_string)
            new_string = new_string.split(',')
            print(new_string)
            # new_string = re.sub(r'\\','',new_string)
            # print(new_string)
            del new_string[0:2]
            new_string = str(new_string).replace("\\","")#преобразует список в строку и если при предыдущем преобразовании строки в список через сплит случился "баг", что апостроф в ключе заменился на косую черту (\) -  то мы возвращаем все как было удалив апострроф 
            new_string = new_string.split(',')
            new_string.pop(1)#удаляет второй ключ(MOBILE или Desktop)
            new_string = str(new_string).replace("\'s","~")
            #new_string = str(new_string).replace("\\","")
            new_string = re.sub("[\[|\]|']","",new_string)
            new_string = new_string.replace("~", "'s")
            new_string = new_string.replace("\\","")
            print(new_string)
            break