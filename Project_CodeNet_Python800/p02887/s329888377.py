N = int(input())
S = input()
i = 0
count = 1
con_s = 0

for i in range(N-1):
  if S[i] in S[i+1]:
    pass
  else:
    count += 1
    
print(count)