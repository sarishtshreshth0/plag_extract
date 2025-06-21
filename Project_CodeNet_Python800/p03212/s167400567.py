import itertools
num=input()
count = 0
for i in range(3, len(num) + 1):
  for j in itertools.product([3,5,7], repeat=i):
    sumj = 0
    for k in range(i):
      sumj += j[k] * (10 ** (i-k-1))
    
    if '3' in (str)(sumj) and '5' in (str)(sumj) and '7' in (str)(sumj):
      if sumj <= (int)(num):
        count += 1
        #print(sumj)
      else:
        break
print(count)