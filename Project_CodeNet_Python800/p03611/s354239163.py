N = int(input())
l = list(map(int, input().split()))

result_list = []
for a in l:
    result_list.extend([a-1,a,a+1])
    
result_list

import collections

count = collections.Counter(result_list) # dictionary としてCounter({5: 1, 1: 3, 3: 2, 2: 2, 4: 2})
hindo_jun = count.most_common() 

print(hindo_jun[0][1])
