from collections import Counter

N = int(input())
a = list(map(int,input().split()))
c = Counter(a)
max_num = 0

for x in range(max(a)+1):
      max_num = max(max_num,(c[x] + c[x+1] + c[x+2]))
print(max_num)
