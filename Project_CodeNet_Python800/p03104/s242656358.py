def xor_sum(n):
    #0からの連続数のXOR和は４つ目が０（初項）
    st =n -n%4
    n_list =[i for i in range(st,n+1)]
    ans =0
    for i in n_list:
        ans ^=i
    return ans
# 初期入力

import sys
input = sys.stdin.readline
A,B = (int(i) for i in input().split())
ans =xor_sum(B) ^xor_sum(A-1)
print(ans)