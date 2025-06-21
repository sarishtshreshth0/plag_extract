A = list(map(int, input().split()))
A = list(map(lambda x: 14 if x == 1 else x, A))

if A[0] > A[1]:
    print("Alice")
elif A[0] == A[1]:
    print("Draw")
else:
    print("Bob")
