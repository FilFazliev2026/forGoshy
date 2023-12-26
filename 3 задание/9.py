a = input('введите номер билетика с чётным количеством цифр ')
b = 0
c = 0
if len(a)%2==0:
    start = len(a)//2
    number1 = a[0:start]
    number2 = a[start:len(a)]
    for i  in range(len(number1)):
        b += int(number1[i])
        c += int(number2[i])
    if b == c:
        print('счастливый')
    else:
        print('ненененен')
        
else:
    print('читай условие')
