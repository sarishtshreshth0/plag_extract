def simulator(n, a, b, s):
    print()
    boolean_list = ['No'] * n
    count = 0
    for i in range(n):
        if s[i]=='a' and count < a+b:
            count += 1
            boolean_list[i] = 'Yes'
        if s[i]=='b' and count < a+b and s[:i].count('b') <b :
            count += 1
            boolean_list[i] = 'Yes'
    
    for _ in boolean_list:
        print(_)

n, a, b = map(int,input().split())
s = input()
simulator(n, a, b, s)