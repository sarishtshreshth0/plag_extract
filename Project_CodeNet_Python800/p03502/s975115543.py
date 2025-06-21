N = int(input())
A = list(str(N))
A = [int(i) for i in A]
a = sum(A)
if N % a == 0:
    print("Yes")
else:
    print("No")
