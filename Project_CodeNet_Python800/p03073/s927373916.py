s = input()
n = len(s)
if n%2 == 0:
    im1 = '01'*(n//2)
    im2 = '10'*(n//2)
else:
    im1 = '01'*(n//2) + '0'
    im2 = '10'*(n//2) + '1'
cnt1 = 0
cnt2 = 0
for i in range(n):
    if s[i] != im1[i]:
        cnt1 += 1
    if s[i] != im2[i]:
        cnt2 += 1
print(min(cnt1,cnt2))