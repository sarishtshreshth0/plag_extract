m,d=map(int,input().split())
month = [i for i in range(1,m+1)]
ct=0
if d<10:
  print(0)
  exit()
for i in range(11,d+1):
  a=int(str(i)[0])
  b=int(str(i)[1])
  if a*b in month and a>=2 and b>=2:
    ct+=1
print(ct)
