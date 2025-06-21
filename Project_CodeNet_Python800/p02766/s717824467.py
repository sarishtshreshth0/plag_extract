#template
def inputlist(): return [int(j) for j in input().split()]
def listinput(): return input().split()
#template
def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)
N,K = inputlist()
print(len(base10to(N,K)))