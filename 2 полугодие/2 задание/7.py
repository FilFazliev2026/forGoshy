class bank:
    def __init__(self, name, number, money):
        self.name = name
        self.number = number
        self.money = money
        # print('селф ',self)
    def deleted(self, d):
        self.money -= (d + d//100)
        print(self.money)
    def app (self,add):
        self.money += add 
        print(self.money)
    def check(self):
        print(self.money)
        

        
tom = bank('Don', 789834934, 40000)
tom.deleted(10000)
tom.app(20000)
tom.check()