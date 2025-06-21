def make_divisors(n):
    #https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def f(a,b):
    str_a = str(a)
    str_b = str(b)
    return(max(len(str_a),len(str_b)))

n = int(input())
yakusu = make_divisors(n)
kazu = (len(yakusu)+1)//2
ans = 11
for j in range(kazu):
    ans = min(ans,f(yakusu[j],yakusu[-(j+1)]))

print(ans)