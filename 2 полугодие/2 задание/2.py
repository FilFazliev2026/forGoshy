class Soda:
    def show_me_soda(self,additive):
        if additive == '':
            print('обычная')
        else:
            print('Газировка с', additive)
            
tom = Soda()
tom.show_me_soda('')