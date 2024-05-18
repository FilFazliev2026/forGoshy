import random

a = int(input(' 1-камень, 2-бумага, 0-ножницы '))
b = random.randint(0, 2)
if a == b:
    print('ничья')
else:
    if a==0 and b==1:
        print('камень')
    elif a == 0 and b==2:
        print('ножницы')
    elif a==1 and b==0:
        print('камень')
    elif a==1 and b==2:
        print('бумага')
    elif a==2 and b==0:
        print('ножницы')
    elif a==2 and b==1:
        print('бумага')
        
        
               

