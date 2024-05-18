class grafiky:
    def s(self, x,y, x1, y1):
        x2=(x1-x)**2
        y2=(y1-y)**2
        s = x2+y2
        print(s)
        
    def leng(self, x,y,x1,y1):
        x3=(x1-x)**2
        y3=(y1-y)**2
        s1 = x3+y3
        print(s1)
        
    def check(self, x,y):
        if x == 0:
            print('лежит на OX')
        elif y==0:
            print('лежит на OY ')
        else:
            print('не лежит ')
grafik = grafiky()
grafik.s(1,2,3,4)
grafik.leng(1,2,3,4)
grafik.check(1,0)  