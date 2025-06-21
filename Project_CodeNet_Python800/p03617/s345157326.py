q, h, s, d = map(int, input().split())
n = int(input())
q_cp = q*8
h_cp = h*4
s_cp = s*2
d_cp = d
ans = 0
if min(q_cp,h_cp,s_cp,d_cp)==q_cp:
    ans+=n*q*4
elif min(q_cp,h_cp,s_cp,d_cp)==h_cp:
    ans+=n*h*2
elif min(q_cp,h_cp,s_cp,d_cp)==s_cp:
    ans+=n*s
else:
    ans += n//2*d
    amari = n%2
    if min(q_cp, h_cp, s_cp) == q_cp:
        ans += amari*q*4
    elif min(q_cp, h_cp, s_cp) == h_cp:
        ans += amari*h*2
    elif min(q_cp, h_cp, s_cp) == s_cp:
        ans += amari*s
print(int(ans))