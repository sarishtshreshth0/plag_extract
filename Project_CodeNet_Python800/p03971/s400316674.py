n, a, b = [int(i) for i in input().split()]
border = a + b
foreign_pass = 0
passed = 0
s = input()
for x in s:
    if passed >= border:
        print('No')
        continue
    if x == 'a':
        print('Yes')
        passed += 1
    elif x == 'b' and foreign_pass < b:
        print('Yes')
        passed += 1
        foreign_pass += 1
    else:
        print('No')
