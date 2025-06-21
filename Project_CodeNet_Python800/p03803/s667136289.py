a, b = map(int, input().split())
power = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
 
a = power.index(a)
b = power.index(b)
 
if a > b:
    print('Alice')
elif a < b:
    print('Bob')
elif a == b:
    print('Draw')