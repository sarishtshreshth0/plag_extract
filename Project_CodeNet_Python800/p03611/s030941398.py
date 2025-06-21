def chk_num(myList,i,n):
    tmp = 0
    if 0<=i-1<n:
        if myList[i-1][0]+1==myList[i][0]:
            tmp += myList[i-1][1]
    if 0<=i<n:
        tmp += myList[i][1]
    if 0<=i+1<n:
        if myList[i][0]+1==myList[i+1][0]:
            tmp += myList[i+1][1]
    return tmp

n = int(input())
a = list(map(int,input().split()))
dic = {}
for i in range(n):
    dic.setdefault(a[i],0)
    dic[a[i]] += 1
#print(dic)
sortedDict = sorted(dic.items())
#print(sortedDict)
ans = 0
for i in range(len(sortedDict)):
    ans = max(ans,chk_num(sortedDict,i,len(sortedDict)))
print(ans)