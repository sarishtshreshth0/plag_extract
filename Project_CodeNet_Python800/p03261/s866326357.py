n = int(input())
W = [input() for i in range(n)]
flg = 1

Word = [W[0]]
for i in range(1,n):
    s = W[i-1]
    t = W[i]
    
    if(s[-1] != t[0] or t in Word): 
        flg = 0
        break
    Word.append(t)
    
if (flg): print("Yes")
else: print("No")

