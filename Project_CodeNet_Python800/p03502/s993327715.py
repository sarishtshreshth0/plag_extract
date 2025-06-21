N = input()
n = int(N)
sum = 0
a = list(N)
for i in range(len(a)):
    sum += int(a[i])

if n%sum==0:
    print('Yes')
else:
    print('No')