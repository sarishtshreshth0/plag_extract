import math

def make_divisors(n):
    lo_d , up_d = [] , []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lo_d.append(i)
            if i != n // i:
                up_d.append( n // i )
        i += 1
    return lo_d + up_d[::-1]

N = int(input())
List = make_divisors(N)
len_a = len(List)
ans = List[ len_a // 2 ]
print( math.floor(math.log(ans , 10)) + 1 )