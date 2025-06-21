def f(X):
    a = 0
    for i in X:
        a += int(i)
    return  a

N = input()

if int(N)%f(N) == 0:
    print("Yes")
else:
    print("No")