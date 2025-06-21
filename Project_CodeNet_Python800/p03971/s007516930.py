n, a, b = map(int, input().split())
l = input()
num_d = num_i = 0
for i in range(n):
    if l[i] == 'c':
        print('No')
    elif l[i] == 'a':
        if num_d+num_i < a+b:
            print('Yes')
            num_d += 1
        else:
            print('No')
    else:
        if num_d+num_i < a+b:
            if num_i < b:
                print('Yes')
                num_i += 1
            else:
                print('No')
        else:
            print('No')