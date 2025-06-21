n = int(input())
A = []
B = []
for i in range(n):
    a,b = map(int,input().split())
    A.append((a,b))
for i in range(n):
    a,b = map(int,input().split())
    B.append((a,b))
A.sort()
B.sort()

ans = 0

for i in B:
    dis = -1
    check = -1
    for j in range(len(A)):
        if i[0] > A[j][0] and i[1] > A[j][1]:
            
            if dis < A[j][1]:
                check = j
                dis = A[j][1]
    if check > -1:
        ans += 1
        A.pop(check)

print(ans)