N = int(input())
A = 100002*[0]

for a in map(int,input().split()):
  A[a-1]+=1
  A[a]+=1
  A[a+1]+=1

print(max(A))