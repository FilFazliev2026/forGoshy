a = [1,5,6,3,9,8]

def change(a):
    number = len(a) - 1
    for i in range(number):
        for j in range(number-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

change(a)
print(a)
