line = input()
a, b = [int(n) for n in line.split()]

if(a==2 or b==2):
    print('No')
else:
    print('Yes')