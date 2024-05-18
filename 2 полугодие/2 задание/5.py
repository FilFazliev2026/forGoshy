class library:
    def __init__(self):
        self.name = ['book1', 'book2', 'book3']
        # print('селф ',self)
    def deleted(self, d):
        a = self.name
        a.remove(d)
        self.name = a
        print(self.name)
    def app (self,add):
        a = self.name
        a.append(add)
        print(self.name)
    def find(self,finding):
        a = self.name
        b = a.count(finding)
        print(b)
        
tom = library()
tom.deleted('book1')
tom.app('book4')
tom.find('book4')