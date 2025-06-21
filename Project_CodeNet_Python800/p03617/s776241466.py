q, h, s, d = map(int, input().split())
n = int(input())
ans = 0
q_per = q / 0.25
h_per = h / 0.5
s_per = s
d_per = d / 2
list = [q_per,h_per,s_per,d_per]
if min(list) == d_per :
    if n%2 == 0:
        ans += d * (n //2)
    else :
        ans += n//2 * d
        n -= n//2
        list.remove(d_per)
        if min(list) == s_per :
            ans += s_per
        elif min(list) == h_per :
            ans += h * 2
        else :
            ans += q * 4
elif min(list) == s_per :
    ans += n * s
elif min(list) == h_per :
    ans += n * 2 * h
else :
    ans += n * 4 * q

print(int(ans))
