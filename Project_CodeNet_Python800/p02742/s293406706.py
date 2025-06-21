import math

x = list(map(int, input().split()))

h = x[0]
w = x[1]

if (h == 1 or w == 1):
    count = 1
else:
    count = math.ceil(h/2) * math.ceil(w/2) + math.floor(h/2) * math.floor(w/2)

'''
for i in range(h):
    if i % 2 == 0:
        count += math.ceil(w/2)
    else:
        count += math.floor(w/2)
'''

print(count)

