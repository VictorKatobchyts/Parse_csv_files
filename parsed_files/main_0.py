import csv
import re
#search_string = "142"
# with open('out.csv', 'w', newline='') as output_file:
#     writer = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
keys = []
def unique(obj: iter):#создание списка из уникальных ключей
    args = []
    for a in obj:
        if a not in args:
            args.append(a)
            yield a
#my_file = open("BabyFile.txt", "w+")
def sorted_keys(l):
    n =[]
    for i in l:
        if i not in n:
            n.append(i)
    return n
with open('C:\\Users\\Sailwork\\Desktop\\parse\\Parse_csv_files\\TestData.csv') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=';')
    for row in csv_read:
        new_string = re.sub("[\|[\]]",'', row[4])
        new_string = new_string.split(',')
        del new_string[0:2]
        keys.append(new_string)    
    sorted_key3 = str(sorted_keys(keys[4]))
    sorted_key3 = sorted_key3.replace("', '","','")
    print(sorted_key3)
    search_key = re.sub("[\[|\]|']","",sorted_key3)
    print(search_key)
    search_key = search_key.split(',')
    search_key[0] = '"'+search_key[0]+'"'
    search_key[1] = '"'+search_key[1]+'"'
    search_key =  str(search_key).replace("', '","','")
    search_key = re.sub("[\|[\]|']","",str(search_key))
    new_search_key = search_key.replace('"',"")#убирает ковычки 
    new_search_key = new_search_key.split(',')#разделяет ключи (на первый ключ - new_search_key[0]() и на второй ключ -new_search_key[1](MOBILE, DESKTOP))
    print(new_search_key[0])

with open('out.csv', 'w', newline='') as output_file:
     writer1 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
     with open('C:\\Users\\Sailwork\\Desktop\\parse\\Parse_csv_files\\parsed_files\\TestData.csv') as csvfile:
         csv_read = csv.reader(csvfile, delimiter=';')
         for row in csv_read:
             if new_search_key[0] in row[4]:#не ищет с ковычками, только внутренние ключи
                 if new_search_key[1] in row[4]:
                    #if дописать условие сравнения длин строк row[4] и того row[4], которое мы получаем при первом прочтении csv-файла и из которого впоследствии извлекаем ключи
                    writer1.writerow(row)