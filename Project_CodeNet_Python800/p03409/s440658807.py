n = int(input())
R = [0]*n
B = [0]*n
for i in range(n): R[i] = [int(j) for j in input().split()]
for i in range(n): B[i] = [int(j) for j in input().split()]
flag = [False]*n
R.sort(key=lambda x:x[1],reverse=True)
B.sort(key=lambda x:x[0])
ans = 0
for i in range(n):
    c,d = B[i]
    for j in range(n):
        if flag[j]: continue 
        a,b = R[j]
        if c > a and d > b:
            ans += 1
            flag[j] = True
            break
print(ans)