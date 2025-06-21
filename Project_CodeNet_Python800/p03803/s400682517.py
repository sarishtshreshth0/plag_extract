A = [i for i in range(2, 14)] + [1]
a, b = map(int, input().split())
c = -1
d = -1
for i in range(len(A)):
    if c == -1 and A[i] == a:
        c = i
    if d == -1 and A[i] == b:
        d = i

if c > d:
    print("Alice")
elif c < d:
    print("Bob")
else:
    print("Draw")