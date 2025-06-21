N,K=map(int,input().split())
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
x2 = Base_10_to_n(N,K)
print(len(x2))
