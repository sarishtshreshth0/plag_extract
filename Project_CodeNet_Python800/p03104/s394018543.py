a,b=map(int, input().split())
  
a1 = a
b1 = b
if(a1%2 == 1) : a1 = a1+1
if(b1%2 == 0) : b1 = b1-1

c = (b1-a1+1)//2 % 2

ans = 0
if(a%2 == 1):ans = ans^a
if(b%2 == 0):ans = ans^b
print(ans^c)