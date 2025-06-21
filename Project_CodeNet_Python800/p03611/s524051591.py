import collections

n=int(input())
a=list(map(int,input().split()))

aa=[]

for i in range(n):
    aa.append(a[i]-1)
    aa.append(a[i])
    aa.append(a[i]+1)
ans_list=collections.Counter(aa)
print(ans_list.most_common()[0][1])