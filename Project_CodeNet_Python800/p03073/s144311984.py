s=input()
n=len(s)
b_start = 0
w_start = 0
for i in range(n):
    if(i%2==0):
        b_start += (s[i]=='1')
        w_start += (s[i]=='0')
    else:
        b_start += (s[i]=='0')
        w_start += (s[i]=='1')

print(min(b_start,w_start))