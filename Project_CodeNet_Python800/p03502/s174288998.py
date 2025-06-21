def func(n):
    return sum(list(map(int,list(str(n)))))

N = int(input())

print("Yes" if N%func(N) == 0 else "No")