N, A, B = map(int, input().split())
count0, count1 = 0, 0
a = input()
for val in a:
    if val is 'a' and count0+count1 < A+B:
        count0 += 1
        print('Yes')
    elif val is 'b' and count1 < B and count0+count1 < A+B:
        count1 += 1
        print('Yes')
    else:
        print('No')
    
