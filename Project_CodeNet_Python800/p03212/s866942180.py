N = int(input())
list = [3, 5, 7]
num = 0

def dfs(S):
  num_S = 0
  for i in range(len(S)):
    num_S += S[len(S)-i-1]*10**i
  if num_S > N:
    return
  else:
    a = [0, 0, 0]
    for i in range(len(S)):
      if S[i] == 3:
        a[0] += 1
      elif S[i] == 5:
        a[1] += 1
      else:
        a[2] += 1
    if a[0] >= 1 and a[1] >= 1 and a[2] >= 1:
      global num
      num += 1
    dfs(S+[3])
    dfs(S+[5])
    dfs(S+[7])
    return

dfs([])
print(num)