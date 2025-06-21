n,a,b = list(map(int, input().split()))
s = input()
success = 0
success_b = 0
for S in s:
    if S == 'a' and success < a + b:
        print('Yes')
        success += 1
    elif S == 'b' and success < a + b and success_b < b:
        print('Yes')
        success += 1
        success_b += 1
    else:
        print('No')