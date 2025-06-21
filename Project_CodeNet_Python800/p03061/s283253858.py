n=int(input())
a=list(map(int,input().split()))
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
from collections import defaultdict
d=defaultdict(int)
op=set(make_divisors(a[0])+make_divisors(a[1]))
next_op=set()
for i in range(n):
    for opi in op:
        if a[i]%opi==0:
            d[opi]+=1
        if d[opi]>=i:
            next_op.add(opi)
    op=next_op
    next_op=set()
print(max(op))
