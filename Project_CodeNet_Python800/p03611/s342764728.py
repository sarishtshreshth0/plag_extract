from collections import Counter
n=int(input())
a=list(map(int,input().split()))
l=[]
for x in a:
    l.append(x-1)
    l.append(x)
    l.append(x+1)
print(Counter(l).most_common(1)[0][1])