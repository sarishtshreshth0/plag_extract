A,B,C,D = map(int,input().split())

Alice = []
for i in range(A,B):
  Alice.append(i)

Bob = []
for s in range(C,D):
  Bob.append(s)

count = 0  
B = B - A

for i in range(B):
  if Alice[i] in Bob:
    count += 1
print(count)