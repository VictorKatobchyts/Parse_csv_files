import csv
count = 1
with open(f'{count}'+".csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])