N=input()
S=list(map(int,N))
X=sum(S)
f=int(N)/X

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

print('Yes' if is_integer_num(f) else 'No')
