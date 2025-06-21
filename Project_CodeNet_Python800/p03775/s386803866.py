N=int(input())

pairs=[]
for i in range(1,int(N**.5)+5):
  if N % i == 0:
    pairs.append((i,N//i))
    
def f(pair):
  return max(len(str(pair[0])),len(str(pair[1])))

print(min(map(f,pairs)))