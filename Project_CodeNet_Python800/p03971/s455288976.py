n, a, b = list(map(int, input().split()))
s = input()

cnt = 0
oversea = 0

for each in s:
    if each == 'a' and cnt < a + b:
        print('Yes')
        cnt += 1
        continue
    if each == 'b' and cnt < a + b and oversea < b:
        print('Yes')
        cnt += 1
        oversea += 1
        continue
    else:
        print('No')