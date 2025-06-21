n = int(input())
a = [input() for i in range(n)]
if n!=len(set(a)): print("No")
else:
    for i in range(1,n):
        if a[i-1][-1]!=a[i][0]:
            print("No")
            break
    else:
        print("Yes")