n,a,b = map(int,input().split())

mod = 10**9+7
total = pow(2,n,mod) - 1 # 制約なしの全パターン_n**2-1※'-1'は0本の花束

# n個からr個を選択した時のパターン総数_組み合わせ重複なし
# n! / (r! * (n-r)!) → nが大き過ぎて出来ない →変形→ n*(n-1)*･･･(n-r+1)/r! ↓関数化
def nCr(n, r, mod):
    numerator=1 #分子_n*(n-1)*･･･(n-r+1)
    for i in range(n-r+1, n+1):
        numerator = (numerator*i) % mod

    denominator=1 #分母_r!
    for j in range(1,r+1):
        denominator = (denominator*j) % mod
    # 剰余の計算において割るとよくない → 割るのではなく逆元を掛ける
    # フェルマーの小定理_pが素数なら整数aのmod pにおける逆元は a**(p-2) ※aとpは互いに素
    return (numerator * pow(denominator,mod-2,mod)) % mod
    
ans = (total - nCr(n,a,mod) - nCr(n,b,mod)) % mod
print(ans)