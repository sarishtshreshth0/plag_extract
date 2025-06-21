import collections
n = int(input())
lis = list(map(int,input().split()))
count = 0

countArray = [0]*n
calc=0

for i in range(n):
    calc += lis[i]
    countArray[i] = calc
    if calc == 0:
        count +=1

c = collections.Counter(countArray)
a = c.most_common()
for i in range(len(c.most_common())):
    counts = a[i][1]
    if counts < 2:
        break
    count += (counts * (counts - 1)) // 2
print(count)