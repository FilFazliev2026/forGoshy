class avia:
        
    def __init__(self):
        self.company = ['company1','company2']
        self.planes = ['plane1','plane2']
        self.ways = ['way1','way2']
        print('компании ',self.company)
        print('самолёты ',self.planes)
        print('маршруты ',self.ways)
    def deleted(self, delcom,delplane,delway):
        self.company.remove(delcom)
        self.planes.remove(delplane)
        self.ways.remove(delway)
    def app (self,addcom,addplane,addway):
        self.company.append(addcom)
        self.planes.append(addplane)
        self.ways.append(addway)
        print(self.company)
        print(self.planes)
        print(self.ways)
    def find(self,findcom,findplane,findway):
        a = self.company.count(findcom)
        b = self.planes.count(findplane)
        c = self.ways.count(findway)
        print(a)
        print(b)
        print(c)
        

tom=avia()    
tom.deleted('company1', 'plane1','way1')
tom.app('company3','plane3','way3')
tom.find('company2','plane2','way2')
