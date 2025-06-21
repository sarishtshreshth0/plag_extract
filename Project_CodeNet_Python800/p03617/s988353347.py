q,h,s,d = list(map(int, input().split()))
n = int(input())

# 1L
cost_per_1L=min(q*4, h*2, s)
# 2L
cost_per_2L=min(cost_per_1L*2, d)

q,r = divmod(n, 2)

print(cost_per_2L*q + cost_per_1L*r)