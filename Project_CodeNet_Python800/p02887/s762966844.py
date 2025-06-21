N=int(input())
S=input()
last = S[0]
cnt = 1
for s in S[1:]:
  if last != s:
    cnt+=1
    last = s
print(cnt)