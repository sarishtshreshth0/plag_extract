n, a, b = map(int, input().split())
S = str(input())

dom = 0
glo = 0

for s in S:
    if (s == 'a') and (dom + glo < a + b):
        print('Yes')
        dom += 1
    elif (s == 'b') and (dom + glo < a + b) and (glo < b):
        print('Yes')
        glo += 1
    else:
        print('No')
