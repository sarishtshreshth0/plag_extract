
n, a, b = map(int, input().split())

mod = 10**9+7

# (2**n-1)-nCa-nCb

sum_n = pow(2, n, mod)-1
# print(sum_n)
child = 1
mother = 1

for i in range(0, a):
    child *= (n-i)
    child %= mod  # 分子

    mother *= (i+1)
    mother %= mod
# print(mother)
# mod-2はフェルマーの小定理によるchild/mother ->child*(mother**(mod-2)) -2が出てくる理由はhttps://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-4-fermat-%E3%81%AE%E5%B0%8F%E5%AE%9A%E7%90%86%E3%81%AB%E3%82%88%E3%82%8B%E9%80%86%E5%85%83%E8%A8%88%E7%AE%97
hate_a = child * pow(mother, mod-2, mod) % mod

child = 1
mother = 1

for i in range(0, b):
    child *= (n-i)
    child %= mod  # 分母

    mother *= (i+1)
    mother %= mod

hate_b = child * pow(mother, mod-2, mod) % mod

print((sum_n-hate_a-hate_b) % mod)
