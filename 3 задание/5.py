a = '+a+b+k+t+ut+'
b = []
u = 0 
k = 1
for i in range (len(a)):
    if a[i]!='+':
        if a[i-1]=='+' and a[i+1]=='+':
            b.append(u)
        else:
            b.append(k)
s = sum(b)
if s==0:
    print('ададада')
else: 
    print('нененеен')