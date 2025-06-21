def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n=int(input())
lst=sorted(map(int,input().split()))

p=make_divisors(lst[0])
q=make_divisors(lst[1])
pq=set(p+q)
pq=sorted(pq)
for i in range(len(pq)-1,-1,-1):
    out=0
    for j in lst:
        if j%pq[i]!=0:
            out+=1
    if out<=1:
        print(pq[i])
        exit()