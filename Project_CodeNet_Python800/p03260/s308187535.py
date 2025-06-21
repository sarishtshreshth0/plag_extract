ab = input()
ab_lis = ab.split()
a = int(ab_lis[0])
b = int(ab_lis[1])

if a * b % 2 == 0:
    print('No')
elif  a * b % 2 > 0:
    print('Yes')