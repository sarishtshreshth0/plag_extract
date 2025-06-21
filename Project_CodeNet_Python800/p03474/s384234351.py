a,b=map(int,input().split())
s=input()
n=[str(i)for i in range(10)]
for i in range(a + b + 1):
 if(i==a and s[i]!='-')or(i!=a and s[i]not in n):
  print('No');exit()
print('Yes')