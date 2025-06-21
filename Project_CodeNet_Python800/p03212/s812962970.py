import itertools
n=int(input())
cnt=0
for j in range(1, len(str(n))+1):
  lst=(list(itertools.product([3, 5, 7], repeat=j)))
  for i in range(len(lst)):
    temp=int("".join(map(str, lst[i])))
    if "3" in str(temp) and "5" in str(temp) and "7" in str(temp) and temp<=n:
      cnt+=1
print(cnt)