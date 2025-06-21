q, h, s, d = map(int, input().split())
n = int(input())
cost = 0

q_ef = q*8
h_ef = h*4
s_ef = s*2

if min(q_ef, h_ef, s_ef, d) == d:
    cost += d * (n//2)
    n %= 2

if min(q_ef, h_ef, s_ef) == q_ef:
    cost += q * (n*4)
elif h_ef <= s_ef:
    cost += h * (n*2)
else:
    cost += s * n

print(cost)
