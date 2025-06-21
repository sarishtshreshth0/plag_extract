n,m= map(int, input().split())
l = list(map(int, input().split()))

l.sort()
# print(l)
list=[]
if n < m:
    for i in range(m - 1):
        list.append(abs(l[i + 1] - l[i]))

    list.sort()
    # print(list)
    print(sum(list[0:(m - n)]))
else:
    print(0)