# coding: utf-8

n, a, b = map(int,input().split())
s = input()

capacity = 0
foreigner = 0
for i in range(n):
    if s[i] == 'a':
        if capacity <= a+b-1:
            print('Yes')
            capacity += 1
        else:
            print('No')
    elif s[i] == 'b':
        if capacity <= a+b-1 and foreigner <= b-1:
            print('Yes')
            capacity += 1
            foreigner += 1
        else:
            print('No')
            foreigner += 1
    else:
        print('No')