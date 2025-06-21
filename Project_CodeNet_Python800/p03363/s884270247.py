N = int(input())
Ai = list(map(int,input().split()))
    
#print(Ai)
def create_list():
  MAXI = N
  
  sn = [0 for _ in range(MAXI+1)]
  judge = 0
  for i in range(1,MAXI+1):
    #print(str(i)+'+1 when '+S[i-1])
    sn[i] = sn[i-1] + Ai[i-1]
     
  return sn

def iCj(i, j):
  mot = 1
  chi = 1
  for x in range(j):
    chi *= i-x
    mot *= x+1
  comb = int(chi/mot)
  return comb


base = create_list()
#print(base)
count = 0
base.sort()
#print(base)
#for i in range(N):
#  for j in range(i+1,N+1):
#    if(base[j]-base[i] == 0):
#      count += 1
    #  print(str(j)+' - '+str(i))
    #else:
    #  print(str(j)+' = '+str(i))
#  print( base[r[i]] - base[l[i]] )#sum(rnum)-sum(lnum) )
i = 0
while(i<N+1):
  this = 1
  j = i+1
  while(j < N+1 and base[j] == base[i]):
    this += 1
    j += 1
  if(this >= 2):
    count += iCj(this,2)
  i += this
print(count)