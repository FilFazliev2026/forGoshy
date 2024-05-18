
file = open("test.txt", 'r')
data = file.readlines()
# print(data[0])

for j in range(len(data)):
    word1 = 0
    if j==0:
        for i in data:
            if data[j]==i:
                word1+=1
        print(data[j], word1)
    if j>0 and data[j]!=data[j-1]:
        for i in data:
            if data[j]==i:
                word1+=1
        print(data[j], word1)
    
    

file.close()