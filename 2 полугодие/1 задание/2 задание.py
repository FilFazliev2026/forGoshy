a = [313,545]
c = []
u = a[0]
while u!=a[1]:
    hardWord = False
    for j in range(2,u//2):
        print(j)
        if u%j==0 and u!=j:
            hardWord=True
            break
    if hardWord == False:
        c.append(u)
    u+=1
s=sum(c)
print(s)