def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def multiple(a, b):
    return a*b // euclid(a, b)

N = int(input())

print(multiple(N,2))