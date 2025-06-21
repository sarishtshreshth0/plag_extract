n, a, b = map(int,input().split())
s = input()
a_pass = 0
b_pass = 0

for i in s:
    if i == 'a' and a_pass + b_pass < a + b:
        print('Yes')
        a_pass += 1
    elif i == 'b' and a_pass + b_pass < a + b and b_pass < b:
        print('Yes')
        b_pass += 1
    else:
        print('No')