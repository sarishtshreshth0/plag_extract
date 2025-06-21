n=int(input())
la=[input()]
res = "Yes"
for i in range(1,n):
    a=input()
    if a in la or a[0]!=la[i-1][-1]:
        res="No"
        break
    la+=[a]
print(res)