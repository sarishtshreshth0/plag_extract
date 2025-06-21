n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

if len(set(a)) == 1:
    print(n)
    exit()

n_dict = {}
min_n = 10**9
max_n = 0
for i in range(n):
    t = a[i]
    if t in n_dict:
        n_dict[t] += 1
    else:
        n_dict[t] = 1
    
    max_n = max(t, max_n)
    min_n = min(t, min_n)

ans = 0
for x in range(min_n+1, max_n+1):
    tmp = 0
    if x-1 in n_dict: tmp += n_dict[x-1]
    if x in n_dict: tmp += n_dict[x]
    if x+1 in n_dict: tmp += n_dict[x+1]
    
    ans = max(ans, tmp)
print(ans)