def f(a,b):
    return max(len(str(a)),len(str(b)))

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

def main():
    n=int(input())
    m=make_divisors(n)
    a=10**10
    for i in m:
        if n//i < i:
            break
        else:
            a=min(a, f(i, n//i))
    print(a)
                
if __name__ == "__main__":
    main()