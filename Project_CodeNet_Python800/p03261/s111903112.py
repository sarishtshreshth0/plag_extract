N = int(input())
A = [input() for _ in range(N)]
now = A[0]
Done = set()
Done.add(A[0])
for a in A[1:]:
    if a in Done:
        print('No')
        exit()
    if now[-1] == a[0]:
        now = a
        Done.add(a)
    else:
        print('No')
        exit()
print('Yes')
