a=['Джон','Локи','Гого','Миха']
b=['Джон','Гого']
for i in range (len(b)):
    if a.count(b[i])>0:
       a.remove(b[i])
print(a)