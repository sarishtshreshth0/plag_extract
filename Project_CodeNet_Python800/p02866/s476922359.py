from collections import Counter

N = input()
D_list = list(map(int, input().split()))

max_D = max(D_list)
cnt_dic = dict(Counter(D_list))

if (D_list[0] == 0) & (cnt_dic.get(0) == 1):
    ans = 1
    for n in range(1, max_D + 1):
        ans *= cnt_dic.get(n - 1, 0)  ** cnt_dic.get(n, 1)
    print(ans % 998244353)
else: 
    print(0)