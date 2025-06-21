Q,H,S,D=map(int,input().split())
o=Q*8;h=H*4;s=S*2;d=D
N=int(input())*100
A=[0]*4;p=0;q=N
 
A=[[25,Q,o],[50,H,h],[100,S,s],[200,D,d]]
A.sort(key=lambda x: x[2])
 
#print(A)
 
i=0
while  q>0:
  if q%A[i][0]==0:
    p=p+(q//A[i][0])*A[i][1]
    q=q-(q//A[i][0])*A[i][0]
    break
  else:
    p=p+(q//A[i][0])*A[i][1]
    q=q-(q//A[i][0])*A[i][0]
    i=i+1
 
print(int(p))