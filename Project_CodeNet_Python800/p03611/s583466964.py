N = int(input())
A = list(map(int,input().split()))
B = (10**5+2)*[0]
ans = []

for a in A:
  B[a]+=1

for a in A:
  ans+=[B[a-1]+B[a]+B[a+1]]

print(max(ans))