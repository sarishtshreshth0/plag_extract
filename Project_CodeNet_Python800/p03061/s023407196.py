"""参考
@ct158603292321　　2019年05月03日に更新
qiita AtCoder ABC125 解説
https://qiita.com/ct158603292321/items/4cddafa5c2500a657ccf
"""
#約数
def make_divisors(n): #約数をリストで返す
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

# 初期入力
import numpy as np
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A_np =np.array(A)

#list(A)の内、任意で2つ選び約数の和集合（公約数ではない）
div_A_2 =make_divisors(A[0]) + make_divisors(A[1])
ans =[]
for i in div_A_2:
    aa= np.count_nonzero(A_np %i ==0) #iで割り切れる要素を数える
    if aa >=N-1:
        ans.append(i)
print(max(ans))