class trianglleChecker:
    def check(self, a,b,c):
        if a+b>c and a+c>b and b+c>a:
            print('Бобёр доволен, можно строить')
        else:
            print('Бобёр не доволен, нельзя строить')
    def minus(self, a,b,c):
        if a<0 or b<0 or c<0:
            print('Бобёр недоволен, нельзя строить с отрицательными числами')
    def letters(self, a,b,c):
        if a.type() == str or b.type() == str or c.type() == str:
            print('Из букв не построишь настоящий треугольник')
     
            
tom = trianglleChecker()
tom.check(10, 50, 45)
tom.minus(10, 50, 45)
tom.letters(10, 50, 45)