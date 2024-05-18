class shop:
    def __init__(self):
        self.name = 'игрушки'
        self.number = 2
        self.cost = 100
    def changeNumber(self, change):
        choosing = input('прибавить или вычесть(+/-) ')
        if choosing == '+':
            self.number += change
            print(self.number)
        if choosing == '-' and change <= self.number:
            self.number -= change
            print(self.number)
        elif change >= self.number:
            print('нет столько товаров')
    def allcost(self):
        all = self.number * self.cost
        print(all)

tom = shop()
tom.changeNumber(12)
tom.allcost()

        
