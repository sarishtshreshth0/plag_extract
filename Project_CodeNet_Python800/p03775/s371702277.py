n = int(input())

#約数取得
def make_divisors(n):
    divisors_keta = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors_keta.append(max(len(str(i)), len(str(n//i))))
            #print(i, n/i, len(str(i)), len(str(n//i)))
        i += 1
    return divisors_keta

keta_min_sort = sorted(make_divisors(n))

#print(keta_min_sort)
print(keta_min_sort[0])