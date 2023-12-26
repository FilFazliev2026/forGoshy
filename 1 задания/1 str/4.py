a = 'бим бам бом бум'
for i in range(len(a)):
    b = a[i]
    c = b.swapcase()
    a[i] = c
    print(c)

