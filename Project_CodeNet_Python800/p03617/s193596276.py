q, h, s, d = map(int, input().split())
n = int(input())

q_l, h_l, s_l = q*4, h*2, s
l = min(q_l, h_l, s_l)
q_2l, h_2l, s_2l, d_2l = q*8, h*4, s*2, d
l2 = min(q_2l, h_2l, s_2l, d_2l)

if n % 2 == 0:
    ans = l2 * (n//2)
else:
    ans = l2 * (n//2) + l * 1
print(ans)