import copy
n = int(input())
ab = sorted([list(map(int,input().split())) for _ in range(n)],reverse=True)
cd = sorted([list(map(int,input().split())) for _ in range(n)],key = lambda x:x[1])
ans = 0
#print(ab,cd)
for i in range(n):
  for j in range(len(cd)):
    if ab[i][0] < cd[j][0] and ab[i][1] < cd[j][1]:
      ans += 1
      cd.remove(cd[j])
      break
print(ans)     
