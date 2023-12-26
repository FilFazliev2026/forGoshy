a = input()
b = input()
if a == b:
    print('ничья')
else:
    if a =='бумага':
        if b =='камень':
            print('1 выйграл')
        else:
            print('2 выйграл')
    if a =='камень':
        if b =='бумага':
            print('2 выйграл')
        else:
            print('1 выйграл')
    if a =='ножницы':
        if b =='бумага':
            print('1 выйграл')
        else:
            print('2 выйграл')
