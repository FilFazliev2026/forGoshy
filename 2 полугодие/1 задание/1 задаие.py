a = 'дай мне дай мне'
b = [] 
a = a.split()

for i in range(len(a)):
    w1 = a[i]
    print(w1)
    if i+1<len(a):
        for j  in range(i,len(a)):
            w2 = a[j]
            print(w2)
            if w2==w1:
                a.remove(a[j])
            
print(a)