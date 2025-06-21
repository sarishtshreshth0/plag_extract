A, B, C, D = map(int, input().split())

x = [i for i in range(A, B+1)] + [i for i in range(C, D+1)]
l = len(x) - len(set(x))
if l > 0:
    print(l-1)
else:
    print(0)