N = int(input())
A = list(map(int,input().split()))
B = 100002*[0]

for a in A:
  B[a-1]+=1
  B[a]+=1
  B[a+1]+=1

print(max(B))