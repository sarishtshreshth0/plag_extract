n, a, b = map(int, input().split())
s = input()

a_reviewed = 0
b_reviewed = 0

for x in s:
    if a_reviewed + b_reviewed < a + b:
        if x == 'a':
            print('Yes')
            a_reviewed += 1
        elif x == 'b' and b_reviewed < b:
            print('Yes')
            b_reviewed += 1
        else:
            print('No')
    else:
        print('No')