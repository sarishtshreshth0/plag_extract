n = int(input())
d_l = list(map(int,input().split()))

count_dict = {}
for i in range(n):
    count_dict[i] = 0
for val in d_l:
    count_dict[val] += 1

if d_l[0] != 0 or count_dict[0] != 1:
    ans = 0
else:
    ans = 1

for i in range(1,n):
    ans = (ans*(count_dict[i-1]**count_dict[i])) %998244353
    if ans == 0:
        break

print(ans)