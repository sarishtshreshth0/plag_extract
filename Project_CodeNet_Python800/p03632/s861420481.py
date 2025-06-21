n = list(map(int, input().split()))
sum = 0
min = min(n)
max = max(n)
len = max - min
sum = n[1]-n[0] + n[3]-n[2]
sum = sum -len
if(sum < 0):
    sum = 0
print(sum)