import math
import random 
word = 'meow'
b = 0
word1=word
letters=[]
ans=[]
while True:
    for i in range (len(word)):
        letter=random.choice(word)
        letters.append(letter)
        word=list(word)
        word.remove(letter)
        word="".join(word)
    b+=1
    word=word1
    if  "".join(letters) not in ans:
        ans.append("".join(letters))
    letters=[]
    if len(ans) == math.factorial(len(word)) :
        break
print(ans)