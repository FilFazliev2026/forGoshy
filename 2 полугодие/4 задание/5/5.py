import csv

def middle( data):
    allNumbers=0
    number = 0
    for row in data:
        # print(row[0])
        if row[0]!= 'п»ї12':
            row1 = row[0]
            start = row1.find(';')
            end =row1.find(';',start+1)
            a=row1[start+1:end]
            
            a1 = int(a)
            allNumbers+=a1
            number+=1
    middleNumber = allNumbers//number
    print('среднее арифметическое:', middleNumber)


           

file = open("file1.csv", "r")

data = csv.reader(file)

# poll(data)
middle(data)

file.close()

1