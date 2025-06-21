c=list(map(int,input().split()))
n=int(input())
for i in range(4):
  for j in range(4-i):
    c[i+j]=min(c[i+j],c[i]*2**j)
print(n//2*c[3]+n%2*c[2])