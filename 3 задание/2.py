a = '&&&&&xdjgddjfgjg??????'
b = ''
for i in range(len(a)):
    c = a[i]
    b=b+c
    if a[i+1]=='!':
        b=b+'!'
        break
    if a[i+1]=='?':
        b=b+'?'
        break
print(b)