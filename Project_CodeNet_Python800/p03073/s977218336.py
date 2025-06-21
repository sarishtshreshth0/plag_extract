s = input()
LEN = len(s)
if LEN == 1:
    print(0)
    exit()
    
even = s[::2]
odd = s[1::2]

ew = even.count('1')
eb = (LEN+1)//2 - ew
ow = odd.count('1')
ob = (LEN)//2 - ow

print(min(eb + ow, ew + ob))