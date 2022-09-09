from dataclasses import replace
import re

string = "[""2022-02-14"",""https://food.allwomenstalk.com/valentines-day-dinners-to-make-for-your-man/"",""valentine's day dinner"",""MOBILE""]"
#new_string = string.split('""')
#print(new_string[1])
new_string = re.sub("[\|[\]]","", string)
#string.replace('[', '')
#print(string.replace(']',' '))
#print(string)
new_string = new_string.split(',')
#del new_string[0:2]
#new_string.remove(',')
print(new_string)