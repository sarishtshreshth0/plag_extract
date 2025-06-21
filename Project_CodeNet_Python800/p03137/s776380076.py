n,m = map(int, input().split(" "))
xList = [int(i) for i in input().split(" ")]
xList = sorted(xList)
dList = [0]
for i in range(len(xList) -1) :
    dList.append(xList[i+1] - xList[i])
dList = sorted(dList, reverse=True)    

for i in range(n-1) :
    dList[i] = 0
    if(i == len(dList) -1) :
        break
print(sum(dList))