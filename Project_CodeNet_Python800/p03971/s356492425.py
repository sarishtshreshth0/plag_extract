N,A,B = map(int, input().split())
*S, = input()

count = 0
bi = 0
for s in S:
    ans = 'No'
    if count < A+B:
        if s == 'a':
            ans = 'Yes'
            count += 1
        if s == 'b' and bi < B:
            ans = 'Yes'
            count += 1
            bi += 1
    print(ans)