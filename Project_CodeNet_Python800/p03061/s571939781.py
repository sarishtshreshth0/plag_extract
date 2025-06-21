def dv(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
N = int(input())
A = list(map(int,input().split()))
l=[]
cnt = 0
for i in set(dv(A[0])+dv(A[1])):
    cnt = 0
    for j in range(len(A)):
        if A[j]%i == 0:
            cnt += 1
    if cnt >= N-1:
        l.append(i)
print(max(l))