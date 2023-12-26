a = int(input())
b = str(a)
f = ':00'
d = input('')
print(b+d)
if d == 'am':
    print('24-часовой формат - '+b+f)
else:
    g = a+12
    y = str(g)
    print('24-часовой формат - '+y+f)