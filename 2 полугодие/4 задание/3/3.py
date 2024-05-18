numberFinish = 0

def degree(numberFinish,number, degr):
    if numberFinish==0:
        numberFinish=number
    if degr==1:
        print(numberFinish)
        return numberFinish
    else:
        
        numberFinish=numberFinish*number
        return  degree(numberFinish,number,degr-1)

degree(numberFinish,2,10)