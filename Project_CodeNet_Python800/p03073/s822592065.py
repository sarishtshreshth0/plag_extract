s = open(0).read().rstrip()

from itertools import cycle

count1 = 0
for c,d in zip(s,cycle('10')):
#     print(c,d)
    if c!= d:
        count1 += 1
        
count2 = 0
for c,d in zip(s,cycle('01')):
#     print(c,d)
    if c!= d:
        count2 += 1

print(min(count1,count2))