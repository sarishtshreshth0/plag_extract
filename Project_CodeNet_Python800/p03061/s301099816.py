from fractions import gcd
from functools import reduce

N = int(input())
A = list(map(int, input().split()))

my_gcd = reduce(gcd, A)
A = [a // my_gcd for a in A]

flag = False
my_gcd_2 = 0
my_gcd_3 = 0

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

for i in range(N):
    a = A[i]
    if my_gcd_2 == 0:
        my_gcd_2 = a
    else:
        if gcd(my_gcd_2, a) == 1:
            if flag is False:
                if i == 1:
                    my_gcd_3 = a
                else:
                    divisors = make_divisors(a)
                    for d in divisors[::-1]:
                        if len([j for j in A[:i] if j % d]) == 1:
                            my_gcd_3 = d
                            break
                flag = True
                continue
            else:
                my_gcd_2 = -1
        if my_gcd_3 and gcd(my_gcd_3, a) == 1:
            my_gcd_3 = -1
        if my_gcd_2:
            my_gcd_2 = gcd(my_gcd_2, a)
        if my_gcd_3:
            my_gcd_3 = gcd(my_gcd_3, a)

else:
    ans_1 = my_gcd * my_gcd_2
    ans_2 = my_gcd * my_gcd_3
    print(max(ans_1, ans_2, my_gcd))