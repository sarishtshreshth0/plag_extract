n,a,b = map(int , input().split())
s = input()
Judgment = 0
rank = 0
overseas=0
for num in range(n):
  if s[num] == 'a' and rank < a+b:
    print('Yes')
    rank = rank+1
  elif s[num] == 'b' and rank < a+b and overseas < b:
    print('Yes')
    rank = rank +1
    overseas = overseas + 1
  else:
    print('No')