
# 組み合わせの総数 p=10**9+7 で割ったあまりを求める 
"""n<10**9 ,r<10**7  ,p は素数"""
def comb(n,r):
    if n-r < r:
        r=n-r
    p=1
    q=1
    for i in range(r):
        p *=n-i #=n(n-1)・・(n-r+1)
        p %= mod
        q *=i+1 #=1・2・・r =r!
        q %=mod
    return p*pow(q,mod-2,mod)


# 初期入力
N,a,b = (int(x) for x in input().split())
mod =10**9 +7

#N種類の花1本以上の組み合わせ全て(0本選ぶは×なので-1)
all = pow(2,N,mod)-1

#嫌いな本数の組み合わせ
comb_a =comb(N,a)
comb_b =comb(N,b)

ans =(all -comb_a -comb_b)% mod
print(ans)