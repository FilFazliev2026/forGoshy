import csv

with open('weather.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        length = 0
        string = row[1:9]

        if len(string[0]) <= 5:
            for i in range(len(string)):
                length += int(string[i])
        print(length//len(string))
    file.close()