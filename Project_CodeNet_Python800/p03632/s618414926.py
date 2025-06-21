A,B,C,D = map(int,input().split())
M = [0]*100

for n in range(A,B):
  M[n-1]+=1
  
for n in range(C,D):
  M[n-1]+=1
  
print(M.count(2))