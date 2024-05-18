import csv

file1 = open("file1.csv", "r")
file2 = open("file2.csv", "r")
file3 = open("file3.csv", "r")

allFiles = []
data1 = file1.read()
data2 = file2.read()
data3 = file3.read()
allFiles.append(data1)
allFiles.append(data2)
allFiles.append(data3)

# Чтение CSV файла
with open('file.csv', 'w') as file:
    writer = csv.writer(file)
    for row in allFiles:
        writer.writerow(row)
    file.close()

with open("file.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()
file1.close()
file2.close()
file3.close()


    

# Запись CSV файла
# data = [
#     ['Name', 'Age', 'City'],
#     ['John', '25', 'New York'],
#     ['Alice', '30', 'London'],
#     ['Bob', '20', 'Paris']
# ]

# with open('file.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for row in data:
#         writer.writerow(row)
