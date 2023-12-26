a='1, 2, 4, 5'
f=1
b=[]
for i in range(len(a)):
    if a[i]!=" " and a[i]!=",":
        n=int(a[i])
        b.append(n)      
print(b)   
for i in b:
    f=f*i
print(f)
