N = int(input())
al = [int(a) for a in input().split()]
a_dic = {}
for a in al:
    num = a_dic.get(a, 0)
    a_dic[a] = num + 1

min_X = min(al)
max_X = max(al)
ans = 0
for X in range(min_X, max_X + 1):
    num = a_dic.get(X-1, 0) + a_dic.get(X, 0) + a_dic.get(X+1, 0)
    if num > ans:
        ans = num

print(ans)
