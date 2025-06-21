n,k=map(int,input().split())
def main(n,k):
    if n//k:
        return main(n//k,k)+str(n%k)
    return str(n%k)
print(len(main(n,k)))