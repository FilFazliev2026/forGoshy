import csv

data = [
    ['Name', 'surname', 'age'],
    ['John', 'Jameson', '25'],
    ['Alice', 'Bulut', '30'],
    ['Bob', 'Marly', '20']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
    file.close()

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    file.close()
    
    
