from collections import Counter
a='GFGFGFGfgdfjgdfkgk'
b = Counter(a.replace(' ','')).most_common(3)
print(b)

