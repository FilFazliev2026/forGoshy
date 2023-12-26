a = 5
b = 4.5
c = str(a*b)
for i  in range(len(c)):
    start = c.find('.')
    d = c[start:-1]
    e = d[i]
    if e == '5' or e == '6' or e == '7' or e == '8' or e == '9':
        print(c)
        break
else:
    c = int()
    print(round(c))

