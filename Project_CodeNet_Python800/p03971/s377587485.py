N,A,B=list(map(int,input().split()))
S=list(input())
t=0
u=0
for i in range(N):
 if S[i]=='a':
     if t<A+B:
         t=t+1
         print("Yes")
     else:
         print("No")
 elif S[i]=='b':
     if t<A+B and B>u:
         t=t+1
         u=u+1
         print('Yes')
     else:
         print('No')
 else:
     print('No')