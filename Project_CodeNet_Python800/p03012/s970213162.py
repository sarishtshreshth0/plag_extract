n = int(input())
w = list(map(int, input().split()))
w_list = []
for i in range(n):
    w_list.append([w[:i],w[i:]])
del w_list[0]
l = []
for j in w_list:
    l.append(abs(sum(j[0])-sum(j[1])))
print(min(l))