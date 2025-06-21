N = int(input())
a = N*[0]

for i in range(1,N):
  C,S,F = map(int,input().split())
  for j in range(i):
    a[j] = max(S,((F+a[j]-1)//F)*F)+C

print(*a,sep="\n")