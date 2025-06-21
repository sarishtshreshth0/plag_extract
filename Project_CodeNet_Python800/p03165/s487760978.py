import numpy as np
def LCS(s,t,rec=False):
  S=np.array(list(s))
  T=np.array(list(t))
  LS,LT=len(S),len(T)
  dp=np.zeros((LS+1,LT+1))
  for n in range(1,LS+1):
    dp[n,1:]=dp[n-1,:-1]+(S[n-1]==T)
    np.maximum(dp[n],dp[n-1],out=dp[n])
    np.maximum.accumulate(dp[n],out=dp[n])
  if rec:
    tmp=[]
    while LS>0 and LT>0:
      if S[LS-1]==T[LT-1]:
        LS,LT=LS-1,LT-1
        tmp.append(S[LS])
      elif dp[LS,LT]==dp[LS-1,LT]:
        LS-=1
      else:
        LT-=1
    return ''.join(reversed(tmp))
  else:
    return dp[LS][LT]
s=input()
t=input()
print(LCS(s,t,True))