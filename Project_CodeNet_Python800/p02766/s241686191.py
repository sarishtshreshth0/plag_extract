X,n = map(int,input().split(" "))
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
a=Base_10_to_n(X, n)
print(len(str(a)))