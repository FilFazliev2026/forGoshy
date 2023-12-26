a = 'Derty_yyf6'
b = []
c = 'сложность пароля - '
f = 1
for i in range(len(p)):
    if a[i].isdigit() == True:
        a.append(f)
        break
for i in range(len(a)):
    if a[i] == '_':
        b.append(f)
        break
if len(a)>7:
    b.append(f)
for i in range(len(a)):
    if a[i].isalpha() == True:
        if a[i] == a[i].upper():
          b.append(f)
          break
for i in range(len(a)):
    if a[i] == ':':
        b.append(f)
        break
s=sum(b)
o=c+str(s)
print(o)
