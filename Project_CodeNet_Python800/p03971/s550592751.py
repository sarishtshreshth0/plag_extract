n, a, b = map(int, input().split())
s = input()
jap_c = 0
ab_c = 0
for i in list(s):
    if i == 'a':
        if jap_c + ab_c < a+b:
            jap_c += 1
            print('Yes')
            continue
    if i == 'b':
        if jap_c + ab_c < a+b:
            if ab_c < b:
                ab_c += 1
                print('Yes')
                continue
    print('No')