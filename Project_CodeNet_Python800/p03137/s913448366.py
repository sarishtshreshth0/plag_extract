n,m=map(int,input().split())
a = list(map(int,input().split()))
# if m == 1:
#     print(0)
#     exit()
a.sort()
# print(a)
b = []
for i in range(m-1):
    b.append(abs(a[i+1]-a[i]))
b.sort()
b.reverse()
# print(b)
ans = sum(b)-sum(b[0:n-1])
print(ans)