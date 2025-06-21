import itertools
N = int(input())
A = [3,5,7]
s = len(str(N))
ALL = []
for keta in range(3,s+1):
  ALL.extend(list(itertools.product(A, repeat=keta)))
#print(ALL)
ans = 0
for num in ALL:
  L = set(num)
  if 3 not in L or 5 not in L or 7 not in L:
    continue
  temp = ""
  for i in num:
    temp += str(i)
  number = int(temp)
  if number <= N:
    #print(number)
    ans += 1
print(ans)