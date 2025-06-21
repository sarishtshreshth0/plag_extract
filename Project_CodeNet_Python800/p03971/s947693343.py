n,a,b = map(int,input().split())
s = input()
c_a = 0
c_b = 0

for v in s:
    if v == 'a' and c_a < a+b:
        c_a += 1
        print('Yes')
    elif v == 'b' and c_a < a+b and c_b < b:
        c_a += 1
        c_b += 1
        print('Yes')
    else:
        print('No')