a = input()
a = a.replace(' ','')
print(a)
b = a[::-1]
if b==a:
    print('палендром')
else:
    print('нененене')
