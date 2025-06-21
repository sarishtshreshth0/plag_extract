n,k = map(int,input().split())
n2 = k
count = 0
while n2 <= n:
  n2*=k
  count+=1
print(count+1)