
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
with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
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
     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
         csv_read = csv.reader(csvfile, delimiter=';')
         for row in csv_read:
             if new_search_key[0] in row[4]:#не ищет с ковычками, только внутренние ключи
                 if new_search_key[1] in row[4]:
                    #if дописать условие сравнения длин строк row[4] и того row[4], которое мы получаем при первом прочтении csv-файла и из которого впоследствии извлекаем ключи
                    writer1.writerow(row)
        #new_string = re.sub("[\|[\]]","", csv_read[4])
        #new_string = new_string.split(',')
        #del new_string[0:2]
        #print(new_string)
        #print(str(new_string))
        #if str(new_string) in csv_read[4]:
            #writer.writerow(csv_read[4])

            # if "valentine's day dinner" in row[4]:
            #     if "MOBILE" in row[4]:
            #         writer.writerow(row)

# with open('out1.csv', 'w', newline='') as output_file:
#     writer1 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "valentine's day dinner recipes" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer1.writerow(row)

# with open('out2.csv', 'w', newline='') as output_file:
#     writer2 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "what are the advantages of walking in the shoes of others" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer2.writerow(row)
# with open('out3.csv', 'w', newline='') as output_file:
#     writer3 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "detox drinks" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer3.writerow(row)

# with open('out4.csv', 'w', newline='') as output_file:
#     writer4 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "st patricks day food ideas" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer4.writerow(row)

# with open('out5.csv', 'w', newline='') as output_file:
#     writer5 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "detox drinks" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer5.writerow(row)

# with open('out6.csv', 'w', newline='') as output_file:
#     writer6 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "st patrick's day desserts" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer6.writerow(row)

# with open('out7.csv', 'w', newline='') as output_file:
#     writer7 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "drawing websites" in row[4]:
#                 if "DESKTOP" in row[4]:
#                     writer7.writerow(row)

# with open('out8.csv', 'w', newline='') as output_file:
#     writer8 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "underrated talents" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer8.writerow(row)

# with open('out9.csv', 'w', newline='') as output_file:
#     writer9 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "flirty valentines day text messages for him" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer9.writerow(row)

# with open('out10.csv', 'w', newline='') as output_file:
#     writer10 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "the little prince" in row[4]:
#                 if "MOBILE" in row[4]:
#                     writer10.writerow(row)

# with open('out11.csv', 'w', newline='') as output_file:
#     writer11 = csv.writer(output_file, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)

#     with open('C:\\Users\\Sailwork\\Desktop\\parse\\TestData.csv') as csvfile:
#         csv_read = csv.reader(csvfile, delimiter=';')
#         for row in csv_read:
#             if "st patrick's day desserts" in row[4]:
#                 if "DESKTOP" in row[4]:
#                     writer11.writerow(row)  #остановился на 43 строчке данных (выполнив ее обработку)
#     #  reader = csv.reader(csvfile)
#     # reader = csv.reader(csvfile)
#     # reader = csv.reader(csvfile)
#     # for row in reader:
#     #     print(row)
   