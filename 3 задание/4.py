a = 'папрпавыпрпа'
b = 0
c = ''
for i in a:
    d = i.isdigit()
    if d == True:
        c+=i
    else:
        if c!='':
           b+=int(c)
           c = '' 
b+=int(c)
print(b)