S = raw_input()
T = raw_input()

def LCS(S, T) :
  dp = [[0 for t in range(len(T)+1)] for s in range(len(S)+1)]
  for s in range(1, len(S)+1) :
    for t in range(1, len(T)+1) : 
      if S[s-1] == T[t-1] : dp[s][t] = dp[s-1][t-1] + 1
      else : dp[s][t] = max(dp[s-1][t], dp[s][t-1])

  #print "      " + '  '.join(list(T))
  #for i in range(len(dp)) : print S[i-1] if i > 0 else " ", dp[i]

  res = ''
  s, t = len(S), len(T)
  while s > 0 and t > 0 :
    if S[s-1] == T[t-1] : 
      res = S[s-1] + res
      s, t = s-1, t-1
    else :
      if dp[s][t-1] > dp[s-1][t] : t -= 1
      else : s -= 1
  
  print res

LCS(S, T)