import itertools,collections
def make_divisors(n):
    divisors = []
    func = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
                func.append(len(str(n//i)))
            else:
                func.append(len(str(i)))

    divisors.sort()
    return func
def main():
    n = int(input())
    div = make_divisors(n)
    print(min(div))

if __name__ == '__main__':
    main()
