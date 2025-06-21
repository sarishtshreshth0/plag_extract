N=int(input())
W=list(map(int,input().split()))
S1=0;S2=0;
diff=[]
for i in range(N):
  S1+=W[i]
  S2=sum(W)-S1
  diff.append(abs(S1-S2))
print(min(diff))