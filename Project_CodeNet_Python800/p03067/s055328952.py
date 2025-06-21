li = list(map(int,input().split()))
if max(li[0],li[1])>li[2]>min(li[0],li[1]):
  print('Yes')
else:
  print('No')